# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-06 11:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0021_auto_20190405_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedticket',
            name='userprofile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]