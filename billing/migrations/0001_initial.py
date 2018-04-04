# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-04 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billing_rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container_feet', models.CharField(blank=True, choices=[('20', '20'), ('40', '40')], max_length=20, null=True)),
                ('lift_on_charges', models.FloatField(default=0.0)),
                ('lift_off_charges', models.FloatField(default=0.0)),
                ('free_days', models.IntegerField()),
                ('rental_amount', models.FloatField(default=0.0)),
                ('rate_per_hour', models.FloatField(default=0.0)),
                ('rate_per_trip', models.FloatField(default=0.0)),
            ],
        ),
    ]
