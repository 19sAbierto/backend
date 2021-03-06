import os
from concurrent import futures

import requests
from celery import shared_task

from helpers.http import raise_for_status


API_HOST = os.getenv('CUSTOM_DISCOURSE_API_HOST')
API_KEY = os.getenv('CUSTOM_DISCOURSE_API_KEY')
AUTH_PARAMS = {'api_key': API_KEY, 'api_username': 'system'}
TIMEOUT = 30


def get_user_ids(exclude_emails=None):
    r = requests.get(API_HOST + '/admin/users.json', params={**AUTH_PARAMS, **{'show_emails': 'true'}}, timeout=TIMEOUT)
    raise_for_status(r)
    exclude_emails = exclude_emails or []
    return [user['id'] for user in r.json() if user['email'] not in exclude_emails]


@shared_task(name='discourse_log_out_users', default_retry_delay=30, max_retries=3)
def discourse_log_out_users():
    from django.conf import settings
    if not settings.ENVIRONMENT == 'production':
        return

    MAX_WORKERS = 10
    user_ids = get_user_ids([
        'kylebebak@gmail.com', 'eduardo@fortana.co', 'support+hostedsite@discourse.org', 'discobot_email', 'no_email'])

    def log_out_user(user_id):
        try:
            r = requests.post(API_HOST + f'/admin/users/{user_id}/log_out', params=AUTH_PARAMS, timeout=TIMEOUT)
            raise_for_status(r)
        except requests.exceptions.RequestException as e:
            return {'exception': str(e)}
        return r.json()

    with futures.ThreadPoolExecutor(MAX_WORKERS) as executor:
        res = executor.map(log_out_user, user_ids)
    return [r for r in res if r]
