# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-17 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0011_auto_20171217_2220'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='locality',
            index=models.Index(fields=['location'], name='map_localit_locatio_2d37f7_idx'),
        ),
    ]
