# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-02 07:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatekeeperapp', '0003_auto_20180330_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='type_of_gate',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Movement Type of Container'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='time_of_entry',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 2, 12, 30, 49, 522731), null=True),
        ),
    ]
