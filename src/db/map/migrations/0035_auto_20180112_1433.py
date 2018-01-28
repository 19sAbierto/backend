# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-12 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0034_auto_20180111_0630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='uuid',
        ),
        migrations.AddField(
            model_name='organization',
            name='secret_key',
            field=models.TextField(blank=True, unique=False),
        ),
    ]