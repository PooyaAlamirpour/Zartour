# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-03 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20181203_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airport',
            name='id',
        ),
        migrations.AlterField(
            model_name='airport',
            name='iata',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
