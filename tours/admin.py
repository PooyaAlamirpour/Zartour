# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from tours.models import TourTag, TourDestination, TourDescription, TourType, TourStatus, TourImage, Tour, TourHotel, TourService

admin.site.register(Tour)
admin.site.register(TourTag)
admin.site.register(TourImage)
admin.site.register(TourDescription)
admin.site.register(TourDestination)
admin.site.register(TourType)
admin.site.register(TourStatus)
admin.site.register(TourHotel)
admin.site.register(TourService)
