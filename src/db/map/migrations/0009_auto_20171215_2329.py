# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-15 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_auto_20171215_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='progress',
            field=models.FloatField(help_text='How many units have been delivered?', null=True),
        ),
        migrations.AlterField(
            model_name='actionlog',
            name='progress',
            field=models.FloatField(help_text='How many units have been delivered?', null=True),
        ),
    ]