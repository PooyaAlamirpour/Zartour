# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from master.models import City, Airline, Country

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Airline)
