# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from hotels.models import City, Country, Hotel, HotelGallery, HotelService

admin.site.register(Hotel)
admin.site.register(HotelGallery)
admin.site.register(HotelService)
