# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from json import dumps
from django.http import HttpResponse
from django.shortcuts import render
from hotels.models import Hotel, Country, City


def hotels(request):
    hotels = Hotel.objects.all()
    tags = Hotel.objects.all()
    countries = Country.objects.all()
    city = None
    if 'city' in request.GET:
        city_id = request.GET['city']
        if city_id != "0" and city_id is not '':
            hotels = hotels.filter(city_id__in= city_id)
            city = City.objects.get(id=city_id)

    # if 'country' in request.GET:
    #     country_id = request.GET['country']
    #     if country_id != "0":
    #         tours = tours.filter(destinations__city__country_id__in= country_id)

    return render(
        request = request,
        template_name= "bilit360/hotels/hotel_list.html",
        context = { 'hotels':hotels, 'tags':tags, 'countries':countries, 'city':city}
    )


def hotel_details(request, hotel_id):
    hotel = Hotel.objects.get(id = hotel_id)
    return render(
        request = request,
        template_name= "bilit360/hotels/hotel_single.html",
        context = { 'hotel':hotel,}
    )


def city_list(request, country_id):
    cities = City.objects.filter(country_id =country_id)
    result_list = list(cities.values('id', 'CityName'))
    return HttpResponse(dumps(result_list))

