# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-29 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_auto_20190329_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourdestination',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.City'),
        ),
    ]
