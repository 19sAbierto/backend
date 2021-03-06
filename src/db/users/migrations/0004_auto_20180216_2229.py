# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-16 22:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0041_remove_action_source'),
        ('users', '0003_auto_20171106_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('full_name', models.TextField(db_index=True, max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationUserToken',
            fields=[
                ('key', models.TextField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.OrganizationUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='staffuser',
            name='full_name',
            field=models.TextField(db_index=True, max_length=100),
        ),
    ]
