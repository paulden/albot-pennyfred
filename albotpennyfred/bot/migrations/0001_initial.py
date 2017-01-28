# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 17:24
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
                ('text', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('time',),
            },
        ),
    ]
