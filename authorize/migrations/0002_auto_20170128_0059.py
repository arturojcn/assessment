# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorize', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meliprofile',
            name='meli_id',
            field=models.IntegerField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
