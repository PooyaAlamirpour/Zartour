# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-01 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_auto_20190401_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='airline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Airline'),
        ),
        migrations.DeleteModel(
            name='Airline',
        ),
    ]