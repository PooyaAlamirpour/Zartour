# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-04 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0009_tour_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourHotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelName', models.CharField(max_length=200)),
                ('hotelStar', models.IntegerField(default=0)),
                ('singlePrice', models.BigIntegerField(default=0)),
                ('doublePrice', models.BigIntegerField(default=0)),
                ('childPrice', models.BigIntegerField(default=0)),
                ('childWOBedPrice', models.BigIntegerField(default=0)),
                ('infPrice', models.BigIntegerField(default=0)),
                ('hotelLink', models.CharField(max_length=300)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.Tour')),
            ],
        ),
    ]