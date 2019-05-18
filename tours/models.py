# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor.fields import RichTextField

from django.db import models
from master.models import City, Airline


class TourDestination(models.Model):
    city = models.ForeignKey(City)


class TourType(models.Model):
    type_name = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.type_name)


class TourTag(models.Model):
    tag = models.CharField(max_length=300)

    def __unicode__(self):
        return unicode(self.tag)


class TourStatus(models.Model):
    status_code = models.IntegerField(default=0)
    status_text = models.CharField(max_length=300)
    is_valid = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode(str(self.status_code) + " :: " +self.status_text)


class Tour(models.Model):
    views = models.IntegerField(default=0)
    title = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=20, null=True, blank=True)
    stay_nights = models.IntegerField(default=0)
    airline = models.ForeignKey(Airline, null=True, blank=True)
    capacity = models.IntegerField(default=0)
    tags = models.ManyToManyField(TourTag, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    min_price = models.BigIntegerField(default=0)
    type = models.ForeignKey(TourType, null=True, blank=True)
    expire_date = models.DateField(blank=True, null=True)
    outband_date = models.DateField(blank=True, null=True)
    outband_time = models.TimeField(blank=True, null=True)
    origin = models.ForeignKey(City, null=True, blank=True)
    return_date = models.DateField(blank=True, null=True)
    return_time = models.TimeField(blank=True, null=True)
    destinations = models.ManyToManyField(TourDestination, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    documents = RichTextField(null=True, blank=True)

    def __unicode__(self):
        return unicode(self.title)


class TourPassenger(models.Model):
    name = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    last_name_en = models.CharField(max_length=100)
    national_code = models.CharField(max_length=10, null=True, blank=True)
    pass_code = models.CharField(max_length=100, null=True, blank=True)
    tour = models.ForeignKey(Tour)


class TourDescription(models.Model):
    documents = models.CharField(max_length=500)
    text = models.CharField(max_length=500)

    def __unicode__(self):
        return unicode(self.text[:10])


class TourImage(models.Model):
    image = models.ImageField()
    alt = models.CharField(max_length=100)
    tour = models.ForeignKey(Tour)

    def __unicode__(self):
        return unicode(self.tour.title + " :: " + str(self.id))


class TourHotel(models.Model):
    hotelName = models.CharField(max_length=200)
    hotelStar = models.IntegerField(default=0)
    singlePrice = models.BigIntegerField(default=0)
    doublePrice = models.BigIntegerField(default=0)
    childPrice = models.BigIntegerField(default=0)
    childWOBedPrice = models.BigIntegerField(default=0)
    infPrice = models.BigIntegerField(default=0)
    hotelLink = models.CharField(max_length=300, null=True, blank=True)
    tour = models.ForeignKey(Tour)
    service = models.ForeignKey("TourService", null=True, blank=True)



class TourService(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return unicode(self.name)





