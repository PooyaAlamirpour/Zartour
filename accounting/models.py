# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from userprofile.models import *
from django.core.urlresolvers import reverse
from random import randint
from django.contrib.sites.shortcuts import get_current_site


class AccountingArticle(models.Model):
    date = models.DateTimeField()
    text = models.CharField(max_length=100)
    amount = models.IntegerField()
    debit = models.ForeignKey("Account", related_name="debits")
    credit = models.ForeignKey("Account", related_name="credits")

    def __unicode__(self):
        return self.debit.name+"=>"+self.credit.name+"("+str(self.amount)+")"


class AccountManager(models.Manager):
    def create_account(self, userprofile):
        return self.get_or_create(profile=userprofile, code="USER"+str(userprofile.mobile),
                                  name=userprofile.first_name+" "+userprofile.last_name)


class Account(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    profile = models.ForeignKey(UserProfile, null=True, blank=True)
    parent = models.ForeignKey("Account", null=True, blank=True, default=None)
    objects=AccountManager()

    def __unicode__(self):
        return self.code+":"+self.name


class Payment(models.Model):
    amount = models.BigIntegerField(default=0)
    creation_date = models.DateField(null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    confirm_code = models.CharField(max_length=20, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.confirm_code = randint(10000, 99999)
        super(Payment, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.invoice_id+"::"+self.amount

    def get_detail_url(self):
        return reverse('accounting:payment_detail', args=(self.pk,))

    def get_call_back_url(self):
        return "http://127.0.0.1:8000/accounting/payment/confirm/"+str(self.confirm_code)+"/"+str(self.id)