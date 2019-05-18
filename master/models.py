# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Country(models.Model):
    CountryCode = models.CharField(max_length=5)
    CountryName= models.CharField(max_length=100)
    CountryEnName= models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.CountryCode + "::" + self.CountryName)

    def as_json(self):
        return {
            "CountryId": int(self.CountryCode)
        }


class City(models.Model):
    CityCode= models.CharField(max_length=5)
    CityName= models.CharField(max_length=50)
    CityEnName= models.CharField(max_length=50)
    CityLatiude= models.CharField(max_length=50)
    CityLongitude= models.CharField(max_length=50)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return unicode(self.CityCode + "::" + self.CityName)

    def as_json(self):
        return {
            "HotelId": 0,
            "CountryId": int(self.country.CountryCode),
            "CityId": int(self.CityCode),
            "Page": 0,
            "PageSize": 3
        }


class Airline(models.Model):
    name_en = models.CharField(max_length=200)
    name_fa = models.CharField(max_length=200)
    iata = models.CharField(max_length=3)
    logo = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return unicode(self.name_en)