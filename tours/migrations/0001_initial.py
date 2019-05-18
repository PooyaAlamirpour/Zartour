# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-08 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('capacity', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TourDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents', models.CharField(max_length=500)),
                ('text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TourDestination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'')),
                ('alt', models.CharField(max_length=100)),
                ('tour_description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tours.TourDescription')),
            ],
        ),
        migrations.CreateModel(
            name='TourPassenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('last_name_en', models.CharField(max_length=100)),
                ('national_code', models.CharField(blank=True, max_length=10, null=True)),
                ('pass_code', models.CharField(blank=True, max_length=100, null=True)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.Tour')),
            ],
        ),
        migrations.CreateModel(
            name='TourProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TourType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='tourprogram',
            name='tour_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.TourType'),
        ),
        migrations.AddField(
            model_name='tourdestination',
            name='tour_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.TourProgram'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.TourProgram'),
        ),
    ]
