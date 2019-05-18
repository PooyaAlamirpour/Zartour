# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from json import dumps
from django.http import HttpResponse
from master.models import City


def city_list(request, country_id):
    cities = City.objects.filter(country_id =country_id)
    result_list = list(cities.values('id', 'CityName'))
    return HttpResponse(dumps(result_list))