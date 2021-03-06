"""
DEPS:
python manage.py loaddata scian_group.json

USAGE:
python manage.py load --load_dir <dir>
python manage.py load --denue_dir <dir>
python manage.py load --denue_file <file>
python manage.py load --locality_csv <file>
python manage.py load --marg_csv <file>
python manage.py load --donors
python manage.py load --reset_marg
"""
import os
import csv

from django.core.management.base import BaseCommand

from helpers.location import geos_location_from_coordinates
from db.map.models import Locality, Municipality, State
from .loaders import load_denue, load_donors, load_marg_data, reset_marg_data


def load_locality(row):
    """Load locality row to DB.
    """
    (cvegeo_state, state_name, cvegeo_municipality, municipality_name, cvegeo_locality, name,
        latitude, longitude, elevation, *rest) = row
    cvegeo_state = cvegeo_state.strip()
    cvegeo_municipality = cvegeo_state + cvegeo_municipality.strip()
    cvegeo = cvegeo_municipality + cvegeo_locality.strip()

    locality = Locality.objects.filter(cvegeo=cvegeo).first()
    if locality is None:
        Locality.objects.create(
            cvegeo=cvegeo, name=name,
            cvegeo_municipality=cvegeo_municipality, municipality_name=municipality_name,
            cvegeo_state=cvegeo_state, state_name=state_name,
            location=geos_location_from_coordinates(float(latitude), float(longitude)),
            elevation=float(elevation),
        )


def load_municipality(row):
    """Load municipality row to DB.
    """
    cvegeo_state, state_name, cvegeo_municipality, municipality_name, *rest = row
    cvegeo_state = cvegeo_state.strip()
    cvegeo_municipality = cvegeo_state + cvegeo_municipality.strip()

    municipality = Municipality.objects.filter(cvegeo_municipality=cvegeo_municipality).first()
    if municipality is None:
        Municipality.objects.create(
            cvegeo_municipality=cvegeo_municipality, municipality_name=municipality_name,
            cvegeo_state=cvegeo_state, state_name=state_name,
        )


def load_state(row):
    """Load state row to DB.
    """
    cvegeo_state, state_name, *rest = row
    cvegeo_state = cvegeo_state.strip()

    state = State.objects.filter(cvegeo_state=cvegeo_state).first()
    if state is None:
        State.objects.create(cvegeo_state=cvegeo_state, state_name=state_name)


def upsert_locality(row, metrics_labels):
    cvegeo, longitude, latitude, state_name, municipality_name, name = row[:6]
    cvegeo = cvegeo.strip()
    metrics = row[6:]

    metrics_dict = {}
    for k, v in zip(metrics_labels, metrics):
        try:
            v = float(v)
        except ValueError:
            pass
        finally:
            metrics_dict[k] = v

    try:
        locality = Locality.objects.get(cvegeo=cvegeo)
    except:
        locality = Locality.objects.create(
            cvegeo=cvegeo,
            location=geos_location_from_coordinates(float(latitude), float(longitude)),
            state_name=state_name,
            municipality_name=municipality_name,
            name=name,
        )
    locality.meta.update(metrics_dict)
    locality.save()


def sync_locality_features(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file, lineterminator='\n')
        first = True
        metrics_labels = []
        for row in reader:
            if first:
                metrics_labels = row[6:]
                first = False
            else:
                upsert_locality(row, metrics_labels)


def load_from_csv(csv_file, source):
    """Read from source file and insert them into DB.
    """
    source_loader = {
        'locality': load_locality,
        'municipality': load_municipality,
        'state': load_state,
        'denue': load_denue,
    }
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file, lineterminator='\n')
        next(reader, None)
        for row in reader:
            source_loader[source](row)


class Command(BaseCommand):
    help = 'Loads or syncs certain DB tables from CSV files'

    def add_arguments(self, parser):
        parser.add_argument('--locality_csv', help='File to update existing locality records')
        parser.add_argument('--load_dir', help='Directory to load loc, state and muni records')
        parser.add_argument('--denue_dir', help='Directory to load establishment records')
        parser.add_argument('--denue_file', help='File to load establishment records')
        parser.add_argument('--marg_csv', help='File to load social marginalization info')
        parser.add_argument('--donors', action='store_true', help='Load default donors')
        parser.add_argument('--reset_marg', action='store_true',
                            help='Reset marg data, but not damage data, for all localities')

    def handle(self, *args, **options):
        locality_csv = options.get('locality_csv')
        load_dir = options.get('load_dir')
        denue_dir = options.get('denue_dir')
        denue_file = options.get('denue_file')
        marg_csv = options.get('marg_csv')
        donors = options.get('donors')
        reset_marg = options.get('reset_marg')

        if reset_marg:
            reset_marg_data()

        if donors:
            load_donors()

        if load_dir is not None:
            print('loading localities, municipalities and states')
            for source in ['locality', 'municipality', 'state']:
                load_from_csv(os.path.join(load_dir, f'{source}.csv'), source)

        if locality_csv is not None:
            print('syncing locality features')
            sync_locality_features(locality_csv)

        if denue_dir is not None:
            print('syncing denue establishment data')
            for f in os.listdir(denue_dir):
                if not f.endswith('.csv'):
                    continue
                print(f)
                load_from_csv(os.path.join(denue_dir, f), 'denue')

        if denue_file is not None:
            print(f'syncing denue establishment data: {denue_file}')
            load_from_csv(denue_file, 'denue')

        if marg_csv is not None:
            print(f'syncing social marg data: {marg_csv}')
            load_marg_data(marg_csv)
