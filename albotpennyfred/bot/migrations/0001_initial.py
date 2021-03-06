# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=60)),
                ('text', models.CharField(max_length=250)),
                ('time', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=250)),
                ('plan_time', models.CharField(max_length=100)),
                ('client_id', models.CharField(max_length=100)),
            ],
        ),
    ]
