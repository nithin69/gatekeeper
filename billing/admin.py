# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class Billing_ratesAdmin(admin.ModelAdmin):
	list_display = ('liner_name', 'container_feet')
	field = '__all__'

admin.site.register(Billing_rates, Billing_ratesAdmin)
#admin.site.register(Billing_containers)
#admin.site.register(Billing_rental)
#admin.site.register(Billing_pre_trip)
#admin.site.register(Billing_transport)


