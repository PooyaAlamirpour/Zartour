# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import DetailView

from CMS.models import Article
from hotels.models import Hotel
from master.models import Country
from service import jalali
from django.shortcuts import render, redirect
from argparse import Namespace
import json
import requests
from django.http import HttpResponse, JsonResponse
from models import *
from django.conf import settings
from service import services
from datetime import datetime
from accounting.models import *
from unidecode import unidecode

from service.services import APIService
from tours.models import TourType
import time

BASE_URL= services.APIService.API_URL + 'Information'
from django.views.decorators.cache import never_cache

# Create your views here.

def fill_airports(request):
    #services.APIService.get_new_token()
    data = {
        "data": "airport"
    }
    headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Client-Token': services.APIService.get_new_token()
               }
    response = requests.post(BASE_URL, json=data, verify=False, headers=headers)
    # response_object = json.loads(response.readall().decode('utf-8'))
    airports = json.loads(response.content)
    for airport_obj in airports:
        Airport.objects.get_or_create(
            iata=airport_obj['iata'],
            country=airport_obj['country'],
            en_country = airport_obj['en_country'],
            name = airport_obj['name'],
            en_name=airport_obj['en_name'],
            airport=airport_obj['airport'],
            lat = airport_obj['lat'],
            lng=airport_obj['lng'],
            order=airport_obj['order']
        )
    # for obj in response_object:
    #     print obj.country
    django_response = HttpResponse(
        content=response,
        status=response.status_code,
        content_type=response.headers['Content-Type']
    )
    return django_response

def fill_airlines(request):
    services.APIService.get_new_token()

    data = {
        "data": "airline"
    }
    headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Client-Token': services.APIService.TOKEN
               }
    response = requests.post(BASE_URL, json=data, verify=False, headers=headers)
    # response_object = json.loads(response.readall().decode('utf-8'))
    airlines = json.loads(response.content)
    for airline_obj in airlines:
        Airline.objects.get_or_create(
            name=airline_obj['name'],
            en_name = airline_obj['en_name'],
            iata = airline_obj['iata'],
            logo = airline_obj['logo'],
        )
    # for obj in response_object:
    #     print obj.country
    django_response = HttpResponse(
        content=response,
        status=response.status_code,
        content_type=response.headers['Content-Type']
    )
    return django_response

def fill_nationality(request):
    nationalities = services.APIService.fill_nationality()
    for nationality in nationalities:
        Nationality.objects.get_or_create(
            name=nationality['c'],
            en_name=nationality['en_name'],
            iso=nationality['iso'],
            iso3=nationality['iso3']
        )
    return JsonResponse(nationalities)

@never_cache
def req(request):
    tickets = None
    return_tickets = None
    ticketRequest = None
    airlines = None
    airplanes = None
    flight_classes = None
    if request.GET.get('ticket_request'):
        ticketRequest = TicketRequest.objects.get(id = request.GET.get('ticket_request'))
        tickets = ticketRequest.outbands.all().order_by("price")
        return_tickets = ticketRequest.returns.all().order_by("price")
        if request.GET.get('airline'):
            queried_airlines = request.GET.getlist('airline')
            tickets = tickets.filter(flight_details__airline__in=queried_airlines)
            return_tickets = return_tickets.filter(flight_details__airline__in=queried_airlines)
        if request.GET.get('operator'):
            queried_operators = request.GET.getlist('operator')
            tickets = tickets.filter(flight_details__operator__in=queried_operators)
            return_tickets = return_tickets.filter(flight_details__operator__in=queried_operators)
        if request.GET.get('flight_class'):
            queried_classes = request.GET.getlist('flight_class')
            queried_classes_letters = FlightClassLetter.objects.filter(class_name__name__in=queried_classes).values('letter').distinct()
            tickets = tickets.filter(flight_details__flight_class__in=queried_classes_letters)
            return_tickets = return_tickets.filter(flight_details__flight_class__in=queried_classes_letters)
        airlines = FlightDetails.objects.filter(flight_details__ticket_request_outband__outbands__in=tickets).values(
            'airline', 'airline_name', 'airline_name_fa', 'airline_name_en').distinct()
        flight_classes = FlightDetails.objects.filter(
            flight_details__ticket_request_outband__outbands__in=tickets).values('flight_class').distinct()
        flight_classes_names = FlightClassName.objects.filter(flightclassletter__letter__in=flight_classes).values('name','name_fa').distinct()
        flight_operators = FlightDetails.objects.filter(
            flight_details__ticket_request_outband__outbands__in=tickets).values('operator').distinct()
        return render(
            request=request,
            template_name="bilit360/ticket/show_tickets.html",
            context={
                'tickets': tickets,
                'return_tickets': return_tickets,
                'ticketRequest': ticketRequest,
                'airlines': airlines,
                'flight_classes_names': flight_classes_names,
                'flight_operators': flight_operators,
            }
        )
    airports = Airport.objects.all().order_by('-order')
    date_str = request.GET['departure']  # The date - 29 Dec 2017
    format_str = '%d-%m-%Y'  # The format
    date_str = datetime.fromtimestamp(float(date_str)/1000).date().strftime('%d-%m-%Y')
    datetime_obj = datetime.strptime(date_str, format_str)
    if request.GET.get('return'):
        date_str_return = request.GET['return']  # The date - 29 Dec 2017
        format_str = '%d-%m-%Y'  # The format
        date_str_return = datetime.fromtimestamp(float(date_str_return)/1000).date().strftime('%d-%m-%Y')
        datetime_obj_return = datetime.strptime(date_str_return, format_str)

        ticketRequest = TicketRequest.objects.create(
            outband_course=Course.objects.create(
                date=datetime_obj,
                departure=Airport.objects.get(iata=request.GET['origin']),
                arrival=Airport.objects.get(iata=request.GET['destination'])
            ),
            return_course = Course.objects.create(
                date=datetime_obj_return,
                arrival = Airport.objects.get(iata=request.GET['origin']),
                departure = Airport.objects.get(iata=request.GET['destination'])
            ),
            adult=int(request.GET['madult']),
            child=int(request.GET['mchildren']),
            inf=int(request.GET['minfant'])
        )
        tickets = ticketRequest.outbands.all()
        return_tickets = ticketRequest.returns.all()
    else:
        ticketRequest = TicketRequest.objects.create(
            outband_course=Course.objects.create(
                date=datetime_obj,
                departure = Airport.objects.get(iata=request.GET['origin']),
                arrival = Airport.objects.get(iata=request.GET['destination'])
            ),
            adult = int(request.GET['madult']),
            child = int(request.GET['mchildren']),
            inf = int(request.GET['minfant'])
        )
        tickets = ticketRequest.outbands.all()
    data = ticketRequest.as_json()
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Client-Token': services.APIService.get_new_token()
    }
    response = requests.post(services.APIService.API_URL + 'LowFareSearch', json=data, verify=False,
                             headers=headers)
    request_obj = json.loads(response.content)
    print request_obj
    ticketRequest.request_code = request_obj['request_code']
    ticketRequest.save()
    print "search request sent and updated"

    data = {"request_id": ticketRequest.request_code}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Client-Token': services.APIService.get_new_token()
    }
    response = requests.post(services.APIService.API_URL + 'FareSearchResult', json=data, verify=False,
                             headers=headers)
    request_obj = json.loads(response.content)
    if 'outbound' in request_obj:
        for ticket in request_obj['outbound']:
            ticketRequest.outbands.create(
                ticket_request_return=None,
                ref_number=ticket['ref_number'],
                price=ticket['price'],
                discount=ticket['discount'],
                discount_percent=ticket['discount_percent'],
                currency_code=ticket['currency_code'],
                capacity=ticket['capacity'],
                flight_type=ticket['flight_type'],
                description=ticket['description'],
                flight_details=FlightDetails.objects.create(
                    flight_number=ticket['flight_details']['flight_number'],
                    flight_class=ticket['flight_details']['class'],
                    cabin=ticket['flight_details']['cabin'],
                    refund=ticket['flight_details']['refund'],
                    operator=ticket['flight_details']['operator'],
                    airline=ticket['flight_details']['airline'],
                    airplane=ticket['flight_details']['airplane'],
                    airline_name_fa=ticket['flight_details']['airline_name_fa'],
                    airline_name_en=ticket['flight_details']['airline_name_en'],
                    airline_name=ticket['flight_details']['airline_name'],
                    source=ticket['flight_details']['source'],
                ),
                departure=AirportDate.objects.create(
                    location_code=ticket['departure']['location_code'],
                    airport_name_fa=ticket['departure']['airport_name_fa'],
                    airport_name_en=ticket['departure']['airport_name_en'],
                    city_name_fa=ticket['departure']['city_name_fa'],
                    city_name_en=ticket['departure']['city_name_en'],
                    country_code=ticket['departure']['country_code'],
                    date=datetime.strptime(ticket['departure']['date'], '%Y-%m-%d'),
                    time=datetime.strptime(ticket['departure']['time'], '%H:%M:%S')
                ),
                arrival=AirportDate.objects.create(
                    location_code=ticket['arrival']['location_code'],
                    airport_name_fa=ticket['arrival']['airport_name_fa'],
                    airport_name_en=ticket['arrival']['airport_name_en'],
                    city_name_fa=ticket['arrival']['city_name_fa'],
                    city_name_en=ticket['arrival']['city_name_en'],
                    country_code=ticket['arrival']['country_code'],
                    date=datetime.strptime(ticket['arrival']['date'], '%Y-%m-%d'),
                    time=datetime.strptime(ticket['arrival']['time'], '%H:%M:%S')
                ),
                # passenger_fare_adult = PassengerFare.objects.create(
                #     fare=ticket['passenger_fare']['adult']['fare'],
                #     fee=ticket['passenger_fare']['adult']['fee'],
                #     tax=ticket['passenger_fare']['adult']['tax'],
                # ),
                # passenger_fare_child = PassengerFare.objects.create(
                #     fare=ticket['passenger_fare']['child']['fare'],
                #     fee=ticket['passenger_fare']['child']['fee'],
                #     tax=ticket['passenger_fare']['child']['tax'],
                # ),
                # passenger_fare_infant =PassengerFare.objects.create(
                #     fare=ticket['passenger_fare']['infant']['fare'],
                #     fee=ticket['passenger_fare']['infant']['fee'],
                #     tax=ticket['passenger_fare']['infant']['tax'],
                # ),
                # baggages = Baggage.objects.create(
                #     baggage_type=ticket['baggages']['type'],
                #     Quantity=ticket['baggages']['Quantity'],
                #     Unit=ticket['baggages']['Unit'],
                # ),
                duration="00:00:00"
            )
            ticketRequest.save()
    if 'return' in request_obj:
        for ticket in request_obj['return']:
            ticketRequest.returns.create(
                ticket_request_outband=None,
                ref_number=ticket['ref_number'],
                price=ticket['price'],
                discount=ticket['discount'],
                discount_percent=ticket['discount_percent'],
                currency_code=ticket['currency_code'],
                capacity=ticket['capacity'],
                flight_type=ticket['flight_type'],
                description=ticket['description'],
                flight_details=FlightDetails.objects.create(
                    flight_number=ticket['flight_details']['flight_number'],
                    flight_class=ticket['flight_details']['class'],
                    cabin=ticket['flight_details']['cabin'],
                    refund=ticket['flight_details']['refund'],
                    operator=ticket['flight_details']['operator'],
                    airline=ticket['flight_details']['airline'],
                    airplane=ticket['flight_details']['airplane'],
                    airline_name_fa=ticket['flight_details']['airline_name_fa'],
                    airline_name_en=ticket['flight_details']['airline_name_en'],
                    airline_name=ticket['flight_details']['airline_name'],
                    source=ticket['flight_details']['source'],
                ),
                departure=AirportDate.objects.create(
                    location_code=ticket['departure']['location_code'],
                    airport_name_fa=ticket['departure']['airport_name_fa'],
                    airport_name_en=ticket['departure']['airport_name_en'],
                    city_name_fa=ticket['departure']['city_name_fa'],
                    city_name_en=ticket['departure']['city_name_en'],
                    country_code=ticket['departure']['country_code'],
                    date=datetime.strptime(ticket['departure']['date'], '%Y-%m-%d'),
                    time=datetime.strptime(ticket['departure']['time'], '%H:%M:%S')
                ),
                arrival=AirportDate.objects.create(
                    location_code=ticket['arrival']['location_code'],
                    airport_name_fa=ticket['arrival']['airport_name_fa'],
                    airport_name_en=ticket['arrival']['airport_name_en'],
                    city_name_fa=ticket['arrival']['city_name_fa'],
                    city_name_en=ticket['arrival']['city_name_en'],
                    country_code=ticket['arrival']['country_code'],
                    date=datetime.strptime(ticket['arrival']['date'], '%Y-%m-%d'),
                    time=datetime.strptime(ticket['arrival']['time'], '%H:%M:%S')
                ),
                # passenger_fare_adult = PassengerFare.objects.create(
                #     fare=ticket['passenger_fare']['adult']['fare'],
                #     fee=ticket['passenger_fare']['adult']['fee'],
                #     tax=ticket['passenger_fare']['adult']['tax'],
                # ),
                # passenger_fare_child = PassengerFare.objects.create(
                #     fare=ticket['passenger_fare']['child']['fare'],
                #     fee=ticket['passenger_fare']['child']['fee'],
                #     tax=ticket['passenger_fare']['child']['tax'],
                # ),
                # passenger_fare_infant =PassengerFare.objects.create(
                #     fare=ticket['passenger_fare']['infant']['fare'],
                #     fee=ticket['passenger_fare']['infant']['fee'],
                #     tax=ticket['passenger_fare']['infant']['tax'],
                # ),
                # baggages = Baggage.objects.create(
                #     baggage_type=ticket['baggages']['type'],
                #     Quantity=ticket['baggages']['Quantity'],
                #     Unit=ticket['baggages']['Unit'],
                # ),
                duration="00:00:00"
            )
            ticketRequest.save()
    airlines = FlightDetails.objects.filter(flight_details__ticket_request_outband__id=ticketRequest.id).values('airline','airline_name','airline_name_fa','airline_name_en').distinct()
    flight_classes = FlightDetails.objects.filter(flight_details__ticket_request_outband__id=ticketRequest.id).values('flight_class').distinct()
    flight_classes_names = FlightClassName.objects.filter(flightclassletter__letter__in=flight_classes).values('name','name_fa').distinct()
    flight_operators = FlightDetails.objects.filter(
        flight_details__ticket_request_outband__outbands__in=tickets).values('operator').distinct()
    tickets = ticketRequest.outbands.all()
    return_tickets = ticketRequest.returns.all()
    return render(
        request = request,
        template_name="bilit360/ticket/show_tickets.html",
        context={
            'tickets': tickets,
            'return_tickets': return_tickets,
            'ticketRequest': ticketRequest,
            'airlines': airlines,
            'flight_classes_names': flight_classes_names,
            'flight_operators': flight_operators,
        }
    )

@never_cache
def search_foreign_airline(request):
    tickets = None
    return_tickets = None
    ticketRequest = None
    airlines = None
    airplanes = None
    flight_classes = None

    if request.GET.get('ticket_request'):
        ticketRequest = TicketRequest.objects.get(id=request.GET.get('ticket_request'))
        tickets = ticketRequest.outbands.all().order_by("price")
        return_tickets = ticketRequest.returns.all().order_by("price")
        if request.GET.get('airline'):
            queried_airlines = request.GET.getlist('airline')
            tickets = tickets.filter(flight_details__airline__in=queried_airlines)
            return_tickets = return_tickets.filter(flight_details__airline__in=queried_airlines)
        if request.GET.get('operator'):
            queried_operators = request.GET.getlist('operator')
            tickets = tickets.filter(flight_details__operator__in=queried_operators)
            return_tickets = return_tickets.filter(flight_details__operator__in=queried_operators)
        if request.GET.get('flight_class'):
            queried_classes = request.GET.getlist('flight_class')
            queried_classes_letters = FlightClassLetter.objects.filter(class_name__name__in=queried_classes).values('letter').distinct()
            tickets = tickets.filter(flight_details__flight_class__in=queried_classes_letters)
            return_tickets = return_tickets.filter(flight_details__flight_class__in=queried_classes_letters)
        airlines = FlightDetails.objects.filter(flight_details__ticket_request_outband__outbands__in=tickets).values(
            'airline', 'airline_name', 'airline_name_fa', 'airline_name_en').distinct()
        flight_classes = FlightDetails.objects.filter(
            flight_details__ticket_request_outband__outbands__in=tickets).values('flight_class').distinct()
        flight_classes_names = FlightClassName.objects.filter(flightclassletter__letter__in=flight_classes).values('name','name_fa').distinct()
        flight_operators = FlightDetails.objects.filter(
            flight_details__ticket_request_outband__outbands__in=tickets).values('operator').distinct()
        return render(
            request=request,
            template_name="bilit360/ticket/show_tickets.html",
            context={
                'tickets': tickets,
                'return_tickets': return_tickets,
                'ticketRequest': ticketRequest,
                'airlines': airlines,
                'flight_classes_names': flight_classes_names,
                'flight_operators': flight_operators,
            }
        )
    airports = Airport.objects.all().order_by('-order')
    date_str = request.GET['departure']  # The date - 29 Dec 2017
    format_str = '%d-%m-%Y'  # The format
    date_str = datetime.fromtimestamp(float(date_str)/1000).date().strftime('%d-%m-%Y')
    datetime_obj = datetime.strptime(date_str, format_str)
    # //////////////////////////////////////////////////////////////
    # data = {
    #     "data": "nationality"
    # }
    # # services.APIService.get_new_token()
    # nationalities = APIService.getForeignList('Information', data)
    # index = 0
    # for airport_obj in nationalities:
    #     index = index + 1
    #     tmp_index = index
    #     if tmp_index >= 114:
    #         hello_man = 5
    #
    #     if airport_obj['en_name'] == 'Sri Lanka':
    #         hello_man = 6
    #     else:
    #         Airport.objects.get_or_create(
    #             name=airport_obj['name'],
    #             en_name=airport_obj['en_name'],
    #             iata=airport_obj['iso3'])
    #
    # # Airport.objects.get_or_create(name='Iran airport', en_name='Iran airport', iata='IKA')
    # Airport.objects.get_or_create(name='Dubai airport', en_name='Dsubai', iata='DXB')
    # Airport.objects.get_or_create(name='Instanbul airport', en_name='Instanbul', iata='IST')
    # //////////////////////////////////////////////////////////////
    if request.GET.get('return'):
        date_str_return = request.GET['return']  # The date - 29 Dec 2017
        format_str = '%d-%m-%Y'  # The format
        date_str_return = datetime.fromtimestamp(float(date_str_return)/1000).date().strftime('%d-%m-%Y')
        datetime_obj_return = datetime.strptime(date_str_return, format_str)

        ticketRequest = TicketRequest.objects.create(
            outband_course=Course.objects.create(
                date=datetime_obj,
                departure=Airport.objects.get(iata=request.GET['origin']),
                arrival=Airport.objects.get(iata=request.GET['destination'])
            ),
            return_course = Course.objects.create(
                date=datetime_obj_return,
                arrival = Airport.objects.get(iata=request.GET['origin']),
                departure = Airport.objects.get(iata=request.GET['destination'])
            ),
            adult=int(request.GET['madult']),
            child=int(request.GET['mchildren']),
            inf=int(request.GET['minfant'])
        )
        tickets = ticketRequest.outbands.all()
        return_tickets = ticketRequest.returns.all()
    else:
        ticketRequest = TicketRequest.objects.create(
            outband_course=Course.objects.create(
                date=datetime_obj,
                departure=Airport.objects.get(iata=request.GET['origin']),
                arrival=Airport.objects.get(iata=request.GET['destination'])
            ),
            adult=int(request.GET['madult']),
            child=int(request.GET['mchildren']),
            inf=int(request.GET['minfant'])
        )
        tickets = ticketRequest.outbands.all()

    data = ticketRequest.as_json()
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Client-Token': services.APIService.get_new_token()
    }
    response = requests.post(services.APIService.API_URL + 'LowFareSearch', json=data, verify=False, headers=headers)
    request_obj = json.loads(response.content)
    print request_obj
    ticketRequest.request_code = request_obj['request_code']
    ticketRequest.save()
    print "search request sent and updated"

    data = {"request_id": ticketRequest.request_code}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Client-Token': services.APIService.get_new_token()
    }
    response = requests.post(services.APIService.API_URL + 'FareSearchResult', json=data, verify=False, headers=headers)
    request_obj = json.loads(response.content)
    if 'outbound' in request_obj:
        for ticket in request_obj['outbound']:
            ticketRequest.outbands.create(
                ticket_request_return=None,
                ref_number=ticket['ref_number'],
                price=ticket['price'],
                discount=ticket['discount'],
                discount_percent=ticket['discount_percent'],
                currency_code=ticket['currency_code'],
                capacity=ticket['capacity'],
                flight_type=ticket['flight_type'],
                description=ticket['description'],
                flight_details=FlightDetails.objects.create(
                    flight_number=ticket['flight_details']['flight_number'],
                    flight_class=ticket['flight_details']['class'],
                    cabin=ticket['flight_details']['cabin'],
                    refund=ticket['flight_details']['refund'],
                    operator=ticket['flight_details']['operator'],
                    airline=ticket['flight_details']['airline'],
                    airplane=ticket['flight_details']['airplane'],
                    airline_name_fa=ticket['flight_details']['airline_name_fa'],
                    airline_name_en=ticket['flight_details']['airline_name_en'],
                    airline_name=ticket['flight_details']['airline_name'],
                    source=ticket['flight_details']['source'],
                ),
                departure=AirportDate.objects.create(
                    location_code=ticket['departure']['location_code'],
                    airport_name_fa=ticket['departure']['airport_name_fa'],
                    airport_name_en=ticket['departure']['airport_name_en'],
                    city_name_fa=ticket['departure']['city_name_fa'],
                    city_name_en=ticket['departure']['city_name_en'],
                    country_code=ticket['departure']['country_code'],
                    date=datetime.strptime(ticket['departure']['date'], '%Y-%m-%d'),
                    time=datetime.strptime(ticket['departure']['time'], '%H:%M:%S')
                ),
                arrival=AirportDate.objects.create(
                    location_code=ticket['arrival']['location_code'],
                    airport_name_fa=ticket['arrival']['airport_name_fa'],
                    airport_name_en=ticket['arrival']['airport_name_en'],
                    city_name_fa=ticket['arrival']['city_name_fa'],
                    city_name_en=ticket['arrival']['city_name_en'],
                    country_code=ticket['arrival']['country_code'],
                    date=datetime.strptime(ticket['arrival']['date'], '%Y-%m-%d'),
                    time=datetime.strptime(ticket['arrival']['time'], '%H:%M:%S')
                ),
                # passenger_fare_adult = PassengerFare.objects.create(
                #     fare=ticket['passenger_fare']['adult']['fare'],
                #     fee=ticket['passenger_fare']['adult']['fee'],
                #     tax=ticket['passenger_fare']['adult']['tax'],
                # ),
                # passenger_fare_child = PassengerFare.objects.create(
                #     fare=ticket['passenger_fare']['child']['fare'],
                #     fee=ticket['passenger_fare']['child']['fee'],
                #     tax=ticket['passenger_fare']['child']['tax'],
                # ),
                # passenger_fare_infant =PassengerFare.objects.create(
                #     fare=ticket['passenger_fare']['infant']['fare'],
                #     fee=ticket['passenger_fare']['infant']['fee'],
                #     tax=ticket['passenger_fare']['infant']['tax'],
                # ),
                # baggages = Baggage.objects.create(
                #     baggage_type=ticket['baggages']['type'],
                #     Quantity=ticket['baggages']['Quantity'],
                #     Unit=ticket['baggages']['Unit'],
                # ),
                duration="00:00:00"
            )
            ticketRequest.save()
    if 'return' in request_obj:
        for ticket in request_obj['return']:
            ticketRequest.returns.create(
                ticket_request_outband=None,
                ref_number=ticket['ref_number'],
                price=ticket['price'],
                discount=ticket['discount'],
                discount_percent=ticket['discount_percent'],
                currency_code=ticket['currency_code'],
                capacity=ticket['capacity'],
                flight_type=ticket['flight_type'],
                description=ticket['description'],
                flight_details=FlightDetails.objects.create(
                    flight_number=ticket['flight_details']['flight_number'],
                    flight_class=ticket['flight_details']['class'],
                    cabin=ticket['flight_details']['cabin'],
                    refund=ticket['flight_details']['refund'],
                    operator=ticket['flight_details']['operator'],
                    airline=ticket['flight_details']['airline'],
                    airplane=ticket['flight_details']['airplane'],
                    airline_name_fa=ticket['flight_details']['airline_name_fa'],
                    airline_name_en=ticket['flight_details']['airline_name_en'],
                    airline_name=ticket['flight_details']['airline_name'],
                    source=ticket['flight_details']['source'],
                ),
                departure=AirportDate.objects.create(
                    location_code=ticket['departure']['location_code'],
                    airport_name_fa=ticket['departure']['airport_name_fa'],
                    airport_name_en=ticket['departure']['airport_name_en'],
                    city_name_fa=ticket['departure']['city_name_fa'],
                    city_name_en=ticket['departure']['city_name_en'],
                    country_code=ticket['departure']['country_code'],
                    date=datetime.strptime(ticket['departure']['date'], '%Y-%m-%d'),
                    time=datetime.strptime(ticket['departure']['time'], '%H:%M:%S')
                ),
                arrival=AirportDate.objects.create(
                    location_code=ticket['arrival']['location_code'],
                    airport_name_fa=ticket['arrival']['airport_name_fa'],
                    airport_name_en=ticket['arrival']['airport_name_en'],
                    city_name_fa=ticket['arrival']['city_name_fa'],
                    city_name_en=ticket['arrival']['city_name_en'],
                    country_code=ticket['arrival']['country_code'],
                    date=datetime.strptime(ticket['arrival']['date'], '%Y-%m-%d'),
                    time=datetime.strptime(ticket['arrival']['time'], '%H:%M:%S')
                ),
                # passenger_fare_adult = PassengerFare.objects.create(
                #     fare=ticket['passenger_fare']['adult']['fare'],
                #     fee=ticket['passenger_fare']['adult']['fee'],
                #     tax=ticket['passenger_fare']['adult']['tax'],
                # ),
                # passenger_fare_child = PassengerFare.objects.create(
                #     fare=ticket['passenger_fare']['child']['fare'],
                #     fee=ticket['passenger_fare']['child']['fee'],
                #     tax=ticket['passenger_fare']['child']['tax'],
                # ),
                # passenger_fare_infant =PassengerFare.objects.create(
                #     fare=ticket['passenger_fare']['infant']['fare'],
                #     fee=ticket['passenger_fare']['infant']['fee'],
                #     tax=ticket['passenger_fare']['infant']['tax'],
                # ),
                # baggages = Baggage.objects.create(
                #     baggage_type=ticket['baggages']['type'],
                #     Quantity=ticket['baggages']['Quantity'],
                #     Unit=ticket['baggages']['Unit'],
                # ),
                duration="00:00:00"
            )
            ticketRequest.save()
    airlines = FlightDetails.objects.filter(flight_details__ticket_request_outband__id=ticketRequest.id).values('airline','airline_name','airline_name_fa','airline_name_en').distinct()
    flight_classes = FlightDetails.objects.filter(flight_details__ticket_request_outband__id=ticketRequest.id).values('flight_class').distinct()
    flight_classes_names = FlightClassName.objects.filter(flightclassletter__letter__in=flight_classes).values('name','name_fa').distinct()
    flight_operators = FlightDetails.objects.filter(flight_details__ticket_request_outband__outbands__in=tickets).values('operator').distinct()
    tickets = ticketRequest.outbands.all()
    return_tickets = ticketRequest.returns.all()
    return render(
        request = request,
        template_name="bilit360/ticket/show_tickets.html",
        context={
            'tickets': tickets,
            'return_tickets': return_tickets,
            'ticketRequest': ticketRequest,
            'airlines': airlines,
            'flight_classes_names': flight_classes_names,
            'flight_operators': flight_operators,
        }
    )



def show_calender(request):
    airports = Airport.objects.all().order_by('-order')
    posts=Article.objects.all()[0:8]
    try:
        domestic_type = TourType.objects.get(id=1)
        domestic_tours = domestic_type.tour_set.all()[:9]
    except:
        pass

    try:
        nondomestic_type = TourType.objects.get(id=2)
        nondomestic_tours = nondomestic_type.tour_set.all()[:9]
    except:
        pass

    hotels = Hotel.objects.all()[:8]
    countries = Country.objects.all()
    now = datetime.now()
    LOGGED_IN = False
    BREAD = False
    INTRO = False
    ALL_TABS = False
    USER = False
    return render(
        request = request,
        template_name="bilit360/index.html",
        context=locals()
    )

def show_tickets(request):
    if request.POST:
        airports = Airport.objects.all().order_by('-order')
        ticketRequest = TicketRequest.objects.create(
            outband_course=Course.objects.create(
                date=jalali.Persian(request.POST['date_y'], request.POST['date_m'], request.POST['date_d']).gregorian_string(),
                departure = Airport.objects.get(iata=request.POST['departure']),
                arrival = Airport.objects.get(iata=request.POST['arrival'])
            ),
            adult = int(request.POST['bozorg_']),
            child = int(request.POST['koodak_']),
            inf = int(request.POST['nozad_'])
        )
        tickets = ticketRequest.outbands.all()
        return render(
            request = request,
            template_name="res/show_tickets.html",
            context=locals()
        )

def ticket_price(request):
    if request.POST:
        ticketRequest = Ticket.objects.get(id = request.POST['ticket_id']).ticket_request_outband

        data = {
            "outbound":{
                "ref_number":request.POST['ref_number']
            },
            "adult":ticketRequest.adult,
            "child":ticketRequest.child,
            "inf":ticketRequest.inf
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Client-Token': services.APIService.get_new_token()
        }
        response = requests.post(services.APIService.API_URL+'AirPrice', json=data, verify=False, headers=headers)
        request_obj = json.loads(response.content)
        total = request_obj['total']
    return render(
        request=request,
        template_name="reservation/book.html",
        context=locals()
    )

def book_form(request):
    now = datetime.now()
    if request.POST:
        ticketRequest = Ticket.objects.get(id=request.POST['ticket_id']).ticket_request_outband
        adults = range(0, ticketRequest.adult)
        infs = range(0, ticketRequest.inf)
        childs = range(0, ticketRequest.child)
        ref_number = request.POST['ref_number']
        ticket = Ticket.objects.get(id=request.POST['ticket_id'])
        if 'return_ref_number' in request.POST:
            return_ref_number = request.POST['return_ref_number']
            return_ticket = Ticket.objects.get(id=request.POST['return_ticket_id'])
        return render(
            request= request,
            template_name="bilit360/ticket/book_form.html",
            context=locals()
        )
    return HttpResponse(reverse('home'))

def cancel(request):
    return render(
        request = request,
        template_name="safarjoo/flight/cancel.html",
        context={}
    )

def book_ticket(request):
    if request.POST:
        ticket = Ticket.objects.filter(ref_number=request.POST['ref_number']).first()
        for i in range(0, ticket.ticket_request_outband.inf):
            ticket.passenger_set.create(
                passenger_type=request.POST['type_i'+ str(i+1)],
                gender=request.POST['gender_i' + str(i+1)],
                #accompanied_by_infant= request.POST['accompanied_by_infant_i' + str(i+1)],
                prefix=request.POST['prefix_i' + str(i+1)],
                given_name = request.POST['given_name_i' + str(i+1)],
                surname = request.POST['surname_i' + str(i+1)],
                persian_given_name = request.POST['persian_given_name_i' + str(i+1)],
                persian_surname = request.POST['persian_surname_i' + str(i+1)],
                birthdate = jalali.Persian(unidecode(request.POST['birthdate_d_i'+ str(i+1)])).gregorian_string(),
                telephone =request.POST['telephone'],
                email = request.POST['email'],
                nationality = "IRN",
                national_id = request.POST['national_id_i' + str(i+1)],
                passport = Passport.objects.create(
                    doc_issue_country="IRN"
                )
            )
        for i in range(0, ticket.ticket_request_outband.child):
            ticket.passenger_set.create(
                passenger_type=request.POST['type_c'+ str(i+1)],
                gender=request.POST['gender_c' + str(i+1)],
                #accompanied_by_infant= request.POST['accompanied_by_infant_c' + str(i+1)],
                prefix=request.POST['prefix_c' + str(i+1)],
                given_name = request.POST['given_name_c' + str(i+1)],
                surname = request.POST['surname_c' + str(i+1)],
                persian_given_name = request.POST['persian_given_name_c' + str(i+1)],
                persian_surname = request.POST['persian_surname_c' + str(i+1)],
                birthdate = jalali.Persian(unidecode(request.POST['birthdate_d_c'+ str(i+1)])).gregorian_string(),
                telephone =request.POST['telephone'],
                email = request.POST['email'],
                nationality = "IRN",
                national_id = request.POST['national_id_c' + str(i+1)],
                passport = Passport.objects.create(
                    doc_issue_country="IRN"
                )
            )
        for i in range(0, ticket.ticket_request_outband.adult):
            ticket.passenger_set.create(
                passenger_type=request.POST['type_a'+ str(i+1)],
                gender=request.POST['gender_a' + str(i+1)],
                #accompanied_by_infant= request.POST['accompanied_by_infant_a' + str(i+1)],
                prefix=request.POST['prefix_a' + str(i+1)],
                given_name = request.POST['given_name_a' + str(i+1)],
                surname = request.POST['surname_a' + str(i+1)],
                persian_given_name = request.POST['persian_given_name_a' + str(i+1)],
                persian_surname = request.POST['persian_surname_a' + str(i+1)],
                birthdate = jalali.Persian(unidecode(request.POST['birthdate_d_a'+ str(i+1)])).gregorian_string(),
                telephone =request.POST['telephone'],
                email = request.POST['email'],
                nationality = "IRN",
                national_id = request.POST['national_id_a' + str(i+1)],
                passport = Passport.objects.create(
                    passport_id=request.POST['national_id_a' + str(i+1)],
                    doc_issue_country="IRN",
                    expire_date=jalali.Persian(unidecode(request.POST['expire_passport_d_a' + str(i + 1)])).gregorian_string()
                )
            )
        TOKEN = services.APIService.get_new_token()

        data = ticket.as_json()
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Client-Token': services.APIService.TOKEN
        }
        response = requests.post(services.APIService.API_URL + 'book', json=data, verify=False, headers=headers)
        request_obj = json.loads(response.content)
        print request_obj
        booked_ticket = BookedTicket.objects.create(
            refrence_id = request_obj['refrence_id'],
            # refrence_id = 1122,
            # payment_total= 1000,
            payment_total= request_obj['payment']['total'],
            ticket = ticket
        )
        booked_ticket.ticket = ticket
        if request.user:
            booked_ticket.userprofile = request.user
        booked_ticket.save()
        # return render(
        #     request = request,
        #     template_name= 'reservation/booked_ticket.html',
        #     context=locals()
        # )
        payment = Payment.objects.create(amount=booked_ticket.payment_total )
        return redirect(booked_ticket.get_detail_url())
        # return render(
        #     request = request,
        #     template_name='safarjoo/payment/bill.html',
        #     context={'ticket': booked_ticket}
        # )
        # base_url = "https://mabna.shaparak.ir:8080/Pay"
        # data = {'TerminalID': 69003362, 'Amount': booked_ticket.payment_total, 'callbackURL':'google.com', 'InvoiceID':1212 }
        # response = requests.post(base_url, data=data)
        #
        # print(response.text)  # TEXT/HTML


def pay(request):
    TerminalID = 69003362
    Amount=10000
    callbackURL='google.com'
    InvoiceID = 1212
    return render(
        request=request,
        template_name='safarjoo/payment/bill2.html',
        context=locals()
    )
    #
    # print(response.text)  # TEXT/HTML


def payment(request):
    services.APIService.get_new_token()

    if request.POST:
        refrence_id = request.POST['ref_id']
        data = {
            'refrence_id':refrence_id
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Client-Token': services.APIService.get_new_token()
        }
        response = requests.post(services.APIService.API_URL + 'Confirm', json=data, verify=False, headers=headers)
        request_obj = json.loads(response.content)
        data_ticket = {
            'reference': refrence_id
        }
        response_ticket = requests.post(services.APIService.API_URL + 'AirDemandTicket', json=data_ticket, verify=False, headers=headers)
        request_obj_ticket = json.loads(response_ticket.content)
        url = request_obj_ticket['flights'][0]['eticket']
        return redirect(url)


class BookedTicketDetails(DetailView):
    context_object_name = 'booked_ticket'
    queryset = BookedTicket.objects.all()
    template_name = "bilit360/ticket/book_confirm.html"



