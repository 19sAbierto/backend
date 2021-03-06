# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 15:42
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20171103_0039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locality',
            old_name='munipality_name',
            new_name='municipality_name',
        ),
        migrations.AlterField(
            model_name='action',
            name='contact',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}, help_text='Contact data'),
        ),
        migrations.AlterField(
            model_name='actionlog',
            name='contact',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}, help_text='Contact data'),
        ),
    ]
