# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-04 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0008_auto_20190401_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
