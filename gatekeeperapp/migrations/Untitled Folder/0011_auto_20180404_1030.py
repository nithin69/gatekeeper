# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-04 05:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatekeeperapp', '0010_auto_20180404_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='time_of_entry',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 4, 10, 30, 41, 168964), null=True),
        ),
    ]