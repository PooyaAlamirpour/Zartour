# -*- coding= utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

from accounting.models import Payment
from userprofile.models import UserProfile
from service.models import *
from service import services

class Airline(models.Model):
    name = models.CharField(max_length=40)
    en_name= models.CharField(max_length=40)
    iata= models.CharField(max_length=5)
    logo= models.CharField(max_length=200)


class Airport(models.Model):
    country= models.CharField(max_length=100)
    en_country= models.CharField(max_length=100)
    name= models.CharField(max_length=100)
    en_name= models.CharField(max_length=100)
    airport= models.CharField(max_length=100)
    iata= models.CharField(max_length=5, primary_key=True)
    lat= models.CharField(max_length=20)
    lng= models.CharField(max_length=20)
    order= models.CharField(max_length=20)

    def __str__(self):
        return self.iata + "::" + self.en_name


class Course(models.Model):
    date=models.DateField()
    departure = models.ForeignKey(Airport, related_name="departure")
    arrival = models.ForeignKey(Airport, related_name="arrival")

    def as_json(self):
        return {
            "date":str(self.date),
            "departure":self.departure.iata,
            "arrival":self.arrival.iata,
        }

    def __str__(self):
        return "("+str(self.date)+")"+"FROM: "+str(self.departure)+" TO: "+str(self.arrival)

class TicketRequest(models.Model):
    outband_course = models.ForeignKey(Course, related_name="outband",null=True, blank=True)
    return_course = models.ForeignKey(Course, related_name="return+", null=True, blank=True)
    adult = models.IntegerField(default=0)
    child = models.IntegerField(default=0)
    inf = models.IntegerField(default=0)
    request_code = models.IntegerField(null=True, blank=True)

    def as_json(self):
        res = None
        if not self.return_course is None:
            res = {
                "outbound":self.outband_course.as_json(),
                "return":self.return_course.as_json(),
                "adult":self.adult,
                "child":self.child,
                "inf":self.inf
            }
        else:
            res = {
                "outbound":self.outband_course.as_json(),
                "adult":self.adult,
                "child":self.child,
                "inf":self.inf
            }

        return res

    def __str__(self):
        return str(self.request_code)

class FlightDetails(models.Model):
    flight_number = models.CharField(max_length=5, null=True, blank=True)
    flight_class = models.CharField(max_length=5, null=True, blank=True)
    cabin = models.CharField(max_length=5, null=True, blank=True)
    refund = models.CharField(max_length=500, null=True, blank=True)
    operator = models.CharField(max_length=30, null=True, blank=True)
    airline = models.CharField(max_length=5, null=True, blank=True)
    airplane = models.CharField(max_length=50, null=True, blank=True)
    airline_name_fa = models.CharField(max_length=50, null=True, blank=True)
    airline_name_en = models.CharField(max_length=50, null=True, blank=True)
    airline_name = models.CharField(max_length=50, null=True, blank=True)
    source = models.CharField(max_length=50, null=True, blank=True)


class AirportDate(models.Model):
    location_code = models.CharField(max_length=5)
    airport_name_fa = models.CharField(max_length=50, null=True, blank=True)
    airport_name_en = models.CharField(max_length=50, null=True, blank=True)
    city_name_fa = models.CharField(max_length=50, null=True, blank=True)
    city_name_en = models.CharField(max_length=50, null=True, blank=True)
    country_code = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()


class PassengerFare(models.Model):
    fare=models.BigIntegerField()
    fee=models.BigIntegerField()
    tax=models.BigIntegerField()


class Baggage(models.Model):
    baggage_type=models.CharField(max_length=5)
    Quantity=models.IntegerField()
    Unit=models.CharField(max_length=5)


class Ticket(models.Model):
    ticket_request_outband = models.ForeignKey(TicketRequest, related_name="outbands", null=True, blank=True)
    ticket_request_return = models.ForeignKey(TicketRequest, related_name="returns", null=True, blank=True)
    ref_number = models.CharField(max_length=100)
    price = models.BigIntegerField()
    discount = models.BigIntegerField()
    discount_percent = models.BigIntegerField()
    currency_code = models.CharField(max_length=5)
    capacity = models.IntegerField()
    flight_type = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    flight_details = models.OneToOneField(FlightDetails, related_name="flight_details")
    departure = models.OneToOneField(AirportDate, related_name="departure")
    arrival = models.OneToOneField(AirportDate, related_name="arrival")
    passenger_fare_adult = models.ForeignKey(PassengerFare, related_name="adult", null=True, blank=True)
    passenger_fare_child = models.ForeignKey(PassengerFare, related_name="child", null=True, blank=True)
    passenger_fare_infant = models.ForeignKey(PassengerFare, related_name="infant", null=True, blank=True)
    baggages = models.OneToOneField(Baggage, null=True, blank=True)
    duration = models.TimeField()

    def as_json(self):
        data = dict()
        data['outbound'] = {
                "ref_number": self.ref_number,
                "departure": self.departure.location_code,
                "arrival": self.arrival.location_code,
                "date": str(self.departure.date) + "T" + str(self.departure.time) + ".000+03:30"
            }
        data['price'] = {
                "currency_code": self.currency_code,
                "total": self.price
            }
        data['passengers']=[]
        for passenger in self.passenger_set.all():
            data['passengers'].append(passenger.as_json())
        return data


class Passport(models.Model):
    passport_id = models.CharField(max_length=30, null=True, blank=True)
    expire_date = models.DateField(null=True, blank=True)
    doc_issue_country = models.CharField(max_length=5,  null=True, blank=True)


class Passenger(models.Model):
    Ticket = models.ForeignKey(Ticket)
    passenger_type = models.CharField(max_length=5)
    gender = models.CharField(max_length=5)
    accompanied_by_infant = models.BooleanField(default=False)
    prefix = models.CharField(max_length=5)
    given_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    persian_given_name= models.CharField(max_length=50)
    persian_surname= models.CharField(max_length=50)
    birthdate = models.DateField()
    telephone = models.CharField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=5)
    national_id = models.CharField(max_length=15)
    passport = models.OneToOneField(Passport, null=True, blank=True)

    def as_json(self):
        data = {
            "type": self.passenger_type,
            "gender": self.gender,
            "accompanied_by_infant": self.accompanied_by_infant,
            "prefix": self.prefix,
            "given_name": self.given_name,
            "surname": self.surname,
            "persian_given_name": self.persian_given_name,
            "persian_surname": self.persian_surname,
            "birthdate": str(self.birthdate),
            "telephone": self.telephone,
            "email": self.email,
            "nationality": self.nationality,
            "national_id": self.national_id,
            "passport": {
                "id": self.passport.passport_id,
                "expire_date": str(self.passport.expire_date),
                "doc_issue_country":self.passport.doc_issue_country
            }
        }
        return data


class BookedTicket(models.Model):
    refrence_id = models.CharField(max_length=30)
    confirmed = models.BooleanField(default=False)
    ticket = models.OneToOneField(Ticket)
    payment_total = models.BigIntegerField()
    payment = models.OneToOneField(Payment, null=True)
    userprofile = models.ForeignKey(UserProfile, blank=True, null=True)

    def get_detail_url(self):
        return reverse('tickets:booked_ticket_details', args=(self.pk,))


class Nationality(models.Model):
    name = models.CharField(max_length=50)
    en_name=models.CharField(max_length=50)
    iso=models.CharField(max_length=2)
    iso3=models.CharField(max_length=3)

    def __str__(self):
        return self.iso + "::" + self.name

#
# class TicketOrder(models.Model):
#     ticket = models.OneToOneField(Ticket)
#
#
#     def __str__(self):
#         return "Ticket Order::" + self.id


class FlightClassName(models.Model):
    name = models.CharField(max_length=200)
    name_fa = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FlightClassLetter(models.Model):
    letter = models.CharField(max_length=5)
    class_name = models.ForeignKey(FlightClassName)

    def __str__(self):
        return self.letter + "::" +self.class_name.name