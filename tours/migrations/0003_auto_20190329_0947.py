# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-29 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_auto_20181227_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='province',
            name='country',
        ),
        migrations.RemoveField(
            model_name='city',
            name='province',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='destination',
        ),
        migrations.AddField(
            model_name='tour',
            name='destinations',
            field=models.ManyToManyField(blank=True, null=True, to='tours.TourDestination'),
        ),
        migrations.AddField(
            model_name='tour',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tour',
            name='expire_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='tours.TourTag'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tourstatus',
            name='status_code',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Province',
        ),
    ]
