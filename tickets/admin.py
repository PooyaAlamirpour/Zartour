# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
# Register your models here.
admin.site.register(Airport)
admin.site.register(Course)
admin.site.register(TicketRequest)
admin.site.register(Ticket)
admin.site.register(Passport)
admin.site.register(Passenger)
admin.site.register(FlightDetails)
admin.site.register(FlightClassName)
admin.site.register(FlightClassLetter)
