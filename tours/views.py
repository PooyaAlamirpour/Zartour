# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from master.models import Country, City
from tours.models import Tour, TourTag


def tours(request):
    tours = Tour.objects.all()
    tags = TourTag.objects.all()
    countries = Country.objects.all()
    city = None
    if 'city' in request.GET:
        city_id = request.GET['city']
        if city_id != "0" and city_id is not '':
            tours = tours.filter(destinations__city_id__in= city_id)
            city = City.objects.get(id=city_id)
    if 'hotelname' in request.GET:
        hotel_name = request.GET['hotelname']
        tours = tours.filter(tourhotel__hotelName__contains=hotel_name)
    # if 'country' in request.GET:
    #     country_id = request.GET['country']
    #     if country_id != "0":
    #         tours = tours.filter(destinations__city__country_id__in= country_id)

    return render(
        request = request,
        template_name= "bilit360/tours/tour_list.html",
        context = { 'tours':tours, 'tags':tags, 'countries':countries, 'city':city}
    )


def tour_details(request, tour_id):
    tour = Tour.objects.get(id = tour_id)
    tour.views = tour.views + 1
    tour.save()
    return render(
        request = request,
        template_name= "bilit360/tours/tour_single.html",
        context = { 'tour':tour,}
    )

