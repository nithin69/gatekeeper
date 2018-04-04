# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-04 05:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cha_shipper', models.CharField(max_length=255, verbose_name=b'Cha/Shipper')),
            ],
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container_no', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Container No.')),
                ('type_of_gate', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Movement Type of Container')),
                ('sz', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Sz & Te')),
                ('csc', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'CSC Plate Details')),
                ('mfg_year', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Mfg Year')),
                ('gr_weight', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Gr. Weight')),
                ('tare_weight', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Tare Weight')),
                ('set_temp', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Set Temp')),
                ('ventilation', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Ventilation')),
                ('humidity', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Humidity')),
                ('action_required', models.CharField(blank=True, choices=[(b'CW', b'CW'), (b'DS', b'DS'), (b'DC', b'DC'), (b'DW', b'DW'), (b'HD', b'HD'), (b'N/A', b'N/A'), (b'SP', b'SP'), (b'WW', b'WW'), (b'3P', b'3P')], max_length=255, null=True, verbose_name=b'Action Required')),
                ('grade', models.CharField(blank=True, choices=[(b'AI', b'AI'), (b'AP', b'AP'), (b'AR', b'AR'), (b'AV', b'AV'), (b'EV', b'EV'), (b'TTL', b'TTL')], max_length=255, null=True, verbose_name=b'Grade')),
                ('status', models.CharField(blank=True, choices=[(b'AI', b'AI'), (b'AP', b'AP'), (b'AR', b'AR'), (b'AV', b'AV'), (b'EV', b'EV'), (b'TTL', b'TTL')], max_length=255, null=True, verbose_name=b'Status')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Location')),
                ('remarks', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Remarks')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255, verbose_name=b'Customer Name')),
            ],
        ),
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.CharField(blank=True, max_length=255, null=True)),
                ('equipmentno', models.CharField(blank=True, max_length=255, null=True)),
                ('size', models.CharField(blank=True, max_length=255, null=True)),
                ('container_size', models.CharField(blank=True, max_length=255, null=True)),
                ('container_type', models.CharField(blank=True, max_length=255, null=True)),
                ('size_feet', models.CharField(blank=True, max_length=255, null=True)),
                ('tareweight', models.CharField(blank=True, max_length=255, null=True)),
                ('cargoweight', models.CharField(blank=True, max_length=255, null=True)),
                ('pin', models.CharField(blank=True, max_length=255, null=True)),
                ('interimpin', models.CharField(blank=True, max_length=255, null=True)),
                ('properties', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.CharField(blank=True, max_length=255, null=True)),
                ('validity_port_date', models.CharField(blank=True, max_length=255, null=True)),
                ('validity_port_time', models.CharField(blank=True, max_length=255, null=True)),
                ('cntr_return_date', models.CharField(blank=True, max_length=255, null=True)),
                ('cntr_return_time', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gate', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Liner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liner', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Liner Name')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_from', models.CharField(max_length=255, verbose_name=b'Place From')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Transporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transporter_name', models.CharField(max_length=255, verbose_name=b'Transporter Name')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('gatepass', models.AutoField(primary_key=True, serialize=False)),
                ('time_of_entry', models.DateTimeField(blank=True, default=datetime.datetime(2018, 4, 4, 11, 9, 18, 287840), null=True)),
                ('vessel_name', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Vessel Name')),
                ('vay_no', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Vay. No.')),
                ('vehicle_no', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Truck No.')),
                ('bill_no', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'BL No.')),
                ('validity_date', models.DateField()),
                ('movement_type', models.CharField(blank=True, choices=[(b'IN', b'IN'), (b'OUT', b'OUT')], max_length=20, null=True)),
                ('surveyor', models.CharField(blank=True, max_length=255, null=True)),
                ('cha', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gatekeeperapp.Cha')),
            ],
            options={
                'verbose_name': 'Entry',
                'verbose_name_plural': 'Entries',
            },
        ),
        migrations.CreateModel(
            name='Yard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yard_name', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_location', models.CharField(blank=True, max_length=255, null=True)),
                ('gate_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gatekeeperapp.Gate')),
            ],
        ),
    ]
