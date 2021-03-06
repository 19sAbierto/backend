from typing import Any
import os
from concurrent import futures
from datetime import timedelta

from django.utils import timezone
from django.db import transaction

import piexif
import requests
from celery import shared_task
from raven.contrib.django.raven_compat.models import client

from db.map.models import Submission, Testimonial, YoutubeAccessToken
from helpers.http import download_file, raise_for_status
from helpers import get_image_size


def video_meta_synced(video):
    return video.get('synced') is True


def image_meta_synced(image):
    return 'exif' in image


def in_s3(url):
    bucket = os.getenv('CUSTOM_AWS_STORAGE_BUCKET_NAME')
    return url.startswith(f'https://{bucket}.s3.amazonaws.com')


def exif_data(image_path):
    try:
        data = piexif.load(image_path)
    except:
        client.captureException()
        return str(None)
    else:
        try:
            del data['thumbnail']
        except:
            pass
        return str(data)


@shared_task(name='sync_submissions_image_meta')
def sync_submissions_image_meta(past_hours=None):
    if past_hours is None:
        submissions = Submission.objects.all()
    else:
        submissions = Submission.objects.filter(created__gt=timezone.now() - timedelta(hours=past_hours))

    for s in submissions:
        if all(image_meta_synced(i) or not in_s3(i['url']) for i in s.images):
            continue
        sync_submission_image_meta.delay(s.id)


@shared_task(name='sync_submission_image_meta')
def sync_submission_image_meta(submission_id):
    MAX_WORKERS = 10
    submission = Submission.objects.get(id=submission_id)

    def get_image_meta(image) -> Any:
        if image_meta_synced(image) or not in_s3(image['url']):
            return image

        url = image['url']
        path = download_file(url, os.path.join(os.sep, 'tmp', url.split('/')[-1]), raise_exception=False)
        if path is None:
            return image

        try:
            meta = get_image_size.get_image_metadata(path)
        except:
            client.captureException()
            width, height, extension = None, None, None
        else:
            width, height, extension = meta.width, meta.height, meta.type

        image['exif'] = exif_data(path)  # pass this string to `ast.literal_eval` to recover exif dict
        image['width'] = width
        image['height'] = height
        image['extension'] = extension
        return image

    with futures.ThreadPoolExecutor(MAX_WORKERS) as executor:
        res = executor.map(get_image_meta, submission.images)
    submission.images = [i for i in res]

    submission.save()


@shared_task(name='sync_testimonial_video_meta', default_retry_delay=30, max_retries=3)
def sync_testimonial_video_meta(testimonial_id):
    def update_video_meta(t):
        if video_meta_synced(t.video):
            return

        url = t.video['url']
        path = download_file(url, os.path.join(os.sep, 'tmp', url.split('/')[-1]))

        name_part = f'de {t.pretty_recipients(3, "y")} ' if t.recipients else ''
        locality = t.action.locality
        site_url = f'{os.getenv("CUSTOM_SITE_URL")}/proyectos/{t.action.id}?_mn=testimonial&_ms={t.id}'
        meta = {
            'snippet': {
                'categoryId': '29',  # nonprofits and activism
                'description': f'Testimonio de un proyecto de {t.action.action_label()} en {locality.name}, {locality.state_name}, realizado por {t.action.organization.name}.\n\n{site_url}',
                'title': f'Testimonio {name_part}en {locality.name}'[:100],  # max title length is 100 chars
            },
            'status': {'privacyStatus': 'public'},
        }
        params = {'part': 'snippet,status', 'uploadType': 'resumable'}

        token = YoutubeAccessToken.objects.get(token_type='Bearer')
        headers = {'Authorization': 'Bearer {}'.format(token.access_token)}

        r = requests.post('https://www.googleapis.com/upload/youtube/v3/videos',
                          json=meta, headers=headers, params=params)
        raise_for_status(r)

        with open(path, 'rb') as data:
            r = requests.post(r.headers['location'], headers=headers, data=data)
            raise_for_status(r)

        data = r.json()
        t.video['synced'] = True
        t.video['youtube_response_data'] = data
        t.video['youtube_video_id'] = data['id']
        try:
            t.video['url_thumbnail'] = data['snippet']['thumbnails']['high']['url']
        except:
            pass
        t.save()

    with transaction.atomic():
        testimonial = Testimonial.objects.select_for_update().get(id=testimonial_id)
        update_video_meta(testimonial)


@shared_task(name='sync_testimonials_video_meta')
def sync_testimonials_video_meta(past_hours=None):
    if past_hours is None:
        testimonials = Testimonial.objects.all()
    else:
        testimonials = Testimonial.objects.filter(created__gt=timezone.now() - timedelta(hours=past_hours))

    for t in testimonials:
        if video_meta_synced(t.video):
            continue
        sync_testimonial_video_meta.delay(t.id)


@shared_task(name='refresh_youtube_access_token', default_retry_delay=30, max_retries=3)
def refresh_youtube_access_token():
    r = requests.post(
        'https://www.googleapis.com/oauth2/v4/token',
        data={
            'client_id': os.getenv('CUSTOM_GOOGLE_OAUTH_CLIENT_ID'),
            'client_secret': os.getenv('CUSTOM_GOOGLE_OAUTH_CLIENT_SECRET'),
            'refresh_token': os.getenv('CUSTOM_GOOGLE_OAUTH_REFRESH_TOKEN'),
            'grant_type': 'refresh_token'
        }
    )
    raise_for_status(r)
    data = r.json()

    try:
        token = YoutubeAccessToken.objects.get(token_type='Bearer')
    except YoutubeAccessToken.DoesNotExist:
        token = YoutubeAccessToken()
    token.access_token = data['access_token']
    token.expires_in = data['expires_in']
    token.token_type = 'Bearer'
    token.save()
