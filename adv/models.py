from django.db import models
from userprofile.models import UserProfile
from userprofile.models import UserProfile
from ckeditor.fields import RichTextField
from userprofile.models import UserProfile

import managers


class AdvType(models.Model):
    starCount = models.IntegerField()
    price = models.IntegerField()


class AdvManager(models.Manager):
    pass


class Adv(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(UserProfile)
    number = models.CharField(max_length=10)
    # simType = models.ForeignKey(SimType)
    # simOperator = models.ForeignKey(SimOperator)
    # simCode = models.ForeignKey(SimCode)
    # simStatus = models.ForeignKey(SimStatus)
    #is_leasable = models.BooleanField(default=False)
    link = models.URLField(null=True)
    #city
    #province
    description = RichTextField()
    email = models.EmailField(null=True)
    price = models.IntegerField(default=True)
    created_date = models.DateTimeField()
    valid_date = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)
    supervisor = models.ForeignKey(UserProfile, related_name="adv_supervisor")
    advType = models.ForeignKey(AdvType)
    objects = AdvManager()


