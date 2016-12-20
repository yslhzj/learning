# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 03:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='timestamp',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2016, 6, 7, 3, 55, 56, 697751, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poem',
            name='updated',
            field=models.DateField(auto_now=True, default=datetime.datetime(2016, 6, 7, 3, 56, 5, 651423, tzinfo=utc)),
            preserve_default=False,
        ),
    ]