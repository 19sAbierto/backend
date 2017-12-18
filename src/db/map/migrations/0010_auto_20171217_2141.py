# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-17 21:41
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0009_auto_20171215_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('cvegeo_municipality', models.TextField(unique=True)),
                ('cvegeo_state', models.TextField(db_index=True)),
                ('municipality_name', models.TextField()),
                ('state_name', models.TextField()),
                ('meta', django.contrib.postgres.fields.jsonb.JSONField(default={}, help_text='Metrics, file URLs, etc')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('cvegeo_state', models.TextField(unique=True)),
                ('state_name', models.TextField()),
                ('meta', django.contrib.postgres.fields.jsonb.JSONField(default={}, help_text='Metrics, file URLs, etc')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='locality',
            name='cvegeo_municipality',
            field=models.TextField(db_index=True, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locality',
            name='cvegeo_state',
            field=models.TextField(db_index=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='locality',
            name='meta',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}, help_text='Metrics, file URLs, etc'),
        ),
        migrations.AlterField(
            model_name='locality',
            name='municipality_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='locality',
            name='state_name',
            field=models.TextField(),
        ),
    ]
