# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-11 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0031_auto_20180111_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
