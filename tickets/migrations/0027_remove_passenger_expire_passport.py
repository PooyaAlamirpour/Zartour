# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-22 12:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0026_auto_20190522_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passenger',
            name='expire_passport',
        ),
    ]