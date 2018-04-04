# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from gatekeeperapp.models import *
import json


class Billing_rates(models.Model):
    container_choice = (
         ('20', '20'),
         ('40', '40'),
        )
    liner_name = models.ForeignKey(Liner)
    container_feet = models.CharField(max_length=20, choices=container_choice, null=True, blank=True)
    lift_on_charges =  models.FloatField(default=0.00)
    lift_off_charges = models.FloatField(default=0.00)
    free_days =  models.IntegerField()
    rental_amount = models.FloatField(default=0.00)
    rate_per_hour = models.FloatField(default=0.00)
    rate_per_trip = models.FloatField(default=0.00)

    def __unicode__(self):
        return str(self.container_feet)

'''
    transportation_charges = models.FloatField(default=0.00)
    
    storage_free  =  models.FloatField(default=0.00)
    storage_free_days  =  models.IntegerField()


    storage_set1  =  models.FloatField(default=0.00)
    storage_set1_days  =  models.IntegerField()


    storage_set2  =  models.FloatField(default=0.00)
    storage_set2_days  =  models.IntegerField()


    storage_choices = (
        ('< 15 days', '< 15 days'),
        (' < 30 days', '< 30 days' ),
        (' < 45 days', '< 45 days' ),
    )

    storage = models.CharField(max_length=20, choices=storage_choices, null=True, blank=True)
    def __unicode__(self):
        return str(self.location_name)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
'''

