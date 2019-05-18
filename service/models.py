from __future__ import unicode_literals

import datetime

from django.db import models
import requests
import json
from userprofile.models import *
from accounting.models import *
# Create your models here.


class ServerException(Exception):
    def __init__(self, message):
        self.message = message


class APIURL(models.Model):
    name = models.CharField(max_length=300)
    api_base_url = models.URLField()

    def __unicode__(self):
        return self.name+":"+self.api_base_url


class APIAddressManager(models.Manager):
    pass


class APIAddress(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    url = models.ForeignKey(APIURL)
    objects = APIAddressManager()

    @property
    def complete_address(self):
        return self.url.api_base_url + self.address

    def __unicode__(self):
        return self.name+":"+self.api_base_url


class APIRequestManager(models.Manager):
    def create_request(self, data, api_address):
        return self.create(date=datetime.now(), data=data, api_address=api_address)

    def get_response(self, request):
        request = self.get(id=request.id)
        response = requests.post(request.api_address.complete_address(), data=request.data)
        if response.ok:
            return json.load(response)
        else:
            raise ServerException(response.status_code+":"+request.api_address.complete_address())


class APIRequest(models.Model):
    date = models.DateTimeField()
    api_address = models.ForeignKey(APIAddress)
    data = models.CharField(max_length=1000)
    response = models.CharField(max_length=1000, blank=True, null=True)
    objects = APIRequestManager()


class JustOneOtherPanelType(models.Model):
    type_id = models.IntegerField(null=True, blank=True)
    type_name = models.CharField(max_length=400)
    type_persian_name = models.CharField(max_length=500, null=True, blank=True)

    def __unicode__(self):
        return self.type_name


class JustOneOtherPanelCategory(models.Model):
    category_id = models.IntegerField(null=True, blank=True)
    category_name = models.CharField(max_length=400)
    category_persian_name = models.CharField(max_length=500, null=True, blank=True)

    def __unicode__(self):
        return self.category_name

class JustOneOtherPanelServiceManager(models.Manager):
    def create_from_obj(self, service):
        category = JustOneOtherPanelCategory.objects.get_or_create(category_name=service.category)[0]
        type = JustOneOtherPanelType.objects.get_or_create(type_name=service.type)[0]
        self.create(category=category, type=type, name=service.name, service_id=int(service.service),
                    rate=float(service.rate), min=int(service.min), max=int(service.max))


class JustOneOtherPanelService(models.Model):
    service_id = models.IntegerField()
    name = models.CharField(max_length=400)
    persian_name = models.CharField(max_length=400, null=True, blank=True)
    rate = models.FloatField()
    min = models.IntegerField()
    max = models.IntegerField()
    category = models.ForeignKey(JustOneOtherPanelCategory)
    type = models.ForeignKey(JustOneOtherPanelType,null=True)
    objects=JustOneOtherPanelServiceManager()

    def __unicode__(self):
        return self.name


class OrderManager(models.Manager):
    def create_order(self, user, service):
        return self.create(user=user, service=service, date=datetime.now())


class Order(models.Model):
    user = models.ForeignKey(UserProfile)
    date = models.DateTimeField()
    service = models.ForeignKey(JustOneOtherPanelService)
    payment = models.OneToOneField(AccountingArticle, null=True, blank=True)
    link = models.URLField()
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    objects = OrderManager()
