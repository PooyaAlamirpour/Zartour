from __future__ import unicode_literals
from random import randint
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from channels.tasks import verify_task_sms, verify_task_call


class UserProfileManager(models.Manager):

    def get_profile(self, user):
        return self.get_or_create(user=user)[0]


class UserProfile(AbstractUser):
    mobile = models.CharField(max_length=11)
    phone = models.IntegerField(blank=True, null=True)
    gender = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    mobile_verified = models.BooleanField(default=False)
    random = models.IntegerField(null=True, blank=True)
    is_ordinary_user = models.BooleanField(default=True)
    code_meli = models.CharField(max_length=20, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.mobile:
            self.username = self.mobile
        super(UserProfile, self).save(*args, **kwargs)
    # objects = UserProfileManager()

    def __unicode__(self):
        return self.mobile

    def send_verify_code(self):
        random = randint(111111, 999999)
        self.set_password(random)
        self.random = random
        self.save()
        print "Profile Password Updated"
        verify_task_sms(self)
        print "SMS Sent"

    def call_verify_code(self):
        random = randint(111111, 999999)
        self.set_password(random)
        self.random = random
        self.save()
        print "Profile Password Updated"
        verify_task_call(self)
        print "Call Sent"


class Supervisor(models.Model):
    user = models.OneToOneField(UserProfile, related_name="supervisor_user")


class Admin(models.Model):
    user = models.OneToOneField(UserProfile, related_name="admin_user")


class Subscriber(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=200, null=True, blank=True)
    domestic_tour = models.BooleanField(default=1)
    subscription_date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return unicode(self.first_name) + " " + unicode(self.last_name) + ": " +unicode(self.mobile)