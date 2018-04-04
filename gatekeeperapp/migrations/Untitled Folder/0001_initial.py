# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-29 03:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gateuser', '0001_initial'),
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
                ('sz', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Sz & Te')),
                ('mty', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Mty / Ldn')),
                ('mfg_year', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Mfg Year')),
                ('gr_weight', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Gr. Weight')),
                ('tare_weight', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Tare Weight')),
                ('action_required', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Action Required')),
                ('grade', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Grade')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Status')),
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
                ('time_of_entry', models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 29, 8, 51, 6, 525133), null=True)),
                ('vessel_name', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Vessel Name')),
                ('vay_no', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Vay. No.')),
                ('vehicle_no', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Truck No.')),
                ('bill_no', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'BL No.')),
                ('validity_date', models.DateField()),
                ('movement_type', models.CharField(blank=True, choices=[(b'IN', b'IN'), (b'OUT', b'OUT')], max_length=20, null=True)),
                ('surveyor', models.CharField(blank=True, max_length=255, null=True)),
                ('cha', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gatekeeperapp.Cha')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='gateuser.Employee')),
                ('customer_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gatekeeperapp.Customer', verbose_name=b'Customer Name')),
                ('gate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gatekeeperapp.Gate')),
                ('line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gatekeeperapp.Liner', verbose_name=b'Liner')),
                ('place_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gatekeeperapp.Place', verbose_name=b'Place From')),
                ('transporter_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gatekeeperapp.Transporter', verbose_name=b'Transporter Name')),
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
        migrations.AddField(
            model_name='container',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gatekeeperapp.Vehicle', verbose_name=b'Vehicle'),
        ),
    ]