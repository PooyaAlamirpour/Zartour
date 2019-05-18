# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.db import models

from master.models import City, Country


class Hotel(models.Model):
    HotelName= models.CharField(max_length=50)
    HotelEnName= models.CharField(max_length=50, null=True, blank=True)
    HotelLatiude= models.CharField(max_length=50, null=True, blank=True)
    HotelLongitude= models.CharField(max_length=50, null=True, blank=True)
    HotelMainImage= models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    HotelStar= models.IntegerField(default=0)
    country = models.ForeignKey(Country, null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    HotelDescription= RichTextField(null=True, blank=True)
    HotelEnDescription= RichTextField(null=True, blank=True)
    HotelSite= models.CharField(max_length=50, null=True, blank=True)
    HotelTell= models.CharField(max_length=50, null=True, blank=True)
    HotelRules= RichTextField(null=True, blank=True)
    HotelAddress= models.CharField(max_length=100, null=True, blank=True)
    HotelFax= models.CharField(max_length=50, null=True, blank=True)
    options = models.ManyToManyField("HotelOption", null=True, blank=True)

    def __unicode__(self):
        return unicode(self.city.CityName + "::" + self.HotelName)


class Room(models.Model):
    room_id = models.CharField(max_length=20)
    hotel = models.ForeignKey(Hotel)


class HotelService(models.Model):
    hotel = models.ForeignKey(Hotel, null=True, blank=True)
    room = models.ForeignKey(Room, null=True, blank=True)
    ServiceCode=models.CharField(max_length=20)
    ServiceName=models.CharField(max_length=20)
    ServiceEnName=models.CharField(max_length=20)
    ServiceDescription=models.CharField(max_length=20)


class HotelGallery(models.Model):
    hotel = models.ForeignKey(Hotel, null=True, blank=True)
    room = models.ForeignKey(Room, null=True, blank=True)
    SmallGalleryUrl=models.CharField(max_length=200, null=True, blank=True)
    MediumGalleryUrl=models.CharField(max_length=200, null=True, blank=True)
    LargeGalleryUrl=models.CharField(max_length=200, null=True, blank=True)
    ThumbnailGalleryUrl=models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return unicode(self.hotel.HotelName + "::" + str(self.id))


class HotelOption(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(null=True, blank=True)


class HotelImage(models.Model):
    image = models.ImageField()
    hotel = models.ForeignKey(Hotel)
