# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-11-29 13:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 29, 13, 40, 30, 908694, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 29, 13, 40, 30, 906970, tzinfo=utc)),
        ),
    ]
