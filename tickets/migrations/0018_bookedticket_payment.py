# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-01-05 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_payment'),
        ('tickets', '0017_airline'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedticket',
            name='payment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.Payment'),
        ),
    ]
