# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-30 05:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatekeeperapp', '0002_auto_20180329_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='container',
            name='mty',
        ),
        migrations.AddField(
            model_name='container',
            name='csc',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'CSC Plate Details'),
        ),
        migrations.AddField(
            model_name='container',
            name='humidity',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Humidity'),
        ),
        migrations.AddField(
            model_name='container',
            name='set_temp',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Set Temp'),
        ),
        migrations.AddField(
            model_name='container',
            name='ventilation',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Ventilation'),
        ),
        migrations.AlterField(
            model_name='container',
            name='action_required',
            field=models.CharField(blank=True, choices=[(b'CW', b'CW'), (b'DS', b'DS'), (b'DC', b'DC'), (b'DW', b'DW'), (b'HD', b'HD'), (b'N/A', b'N/A'), (b'SP', b'SP'), (b'WW', b'WW'), (b'3P', b'3P')], max_length=255, null=True, verbose_name=b'Action Required'),
        ),
        migrations.AlterField(
            model_name='container',
            name='grade',
            field=models.CharField(blank=True, choices=[(b'AI', b'AI'), (b'AP', b'AP'), (b'AR', b'AR'), (b'AV', b'AV'), (b'EV', b'EV'), (b'TTL', b'TTL')], max_length=255, null=True, verbose_name=b'Grade'),
        ),
        migrations.AlterField(
            model_name='container',
            name='status',
            field=models.CharField(blank=True, choices=[(b'AI', b'AI'), (b'AP', b'AP'), (b'AR', b'AR'), (b'AV', b'AV'), (b'EV', b'EV'), (b'TTL', b'TTL')], max_length=255, null=True, verbose_name=b'Status'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='time_of_entry',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 30, 11, 12, 39, 104724), null=True),
        ),
    ]