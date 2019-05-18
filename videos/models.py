# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AparatVideo(models.Model):
    video_id = models.CharField(max_length=30)
    title= models.CharField(max_length=300)
    username = models.CharField(max_length=300)
    userid= models.CharField(max_length=30)
    visit_cnt= models.IntegerField()
    uid= models.CharField(max_length=30)
    isHidden = models.BooleanField()
    process = models.CharField(max_length=30)
    sender_name= models.CharField(max_length=30)
    big_poster= models.CharField(max_length=300)
    small_poster= models.CharField(max_length=300)
    profilePhoto= models.CharField(max_length=300)
    duration= models.CharField(max_length=30)
    sdate= models.CharField(max_length=30)
    create_date= models.CharField(max_length=30)
    sdate_timediff= models.IntegerField()
    frame= models.CharField(max_length=300)
    official= models.CharField(max_length=30)
    autoplay= models.BooleanField()
    video_date_status= models.CharField(max_length=30)
    v_360d=models.BooleanField()
    deleteurl= models.CharField(max_length=300)

    def __unicode__(self):
        return self.video_id