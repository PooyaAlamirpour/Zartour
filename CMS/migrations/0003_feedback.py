# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-11 09:20
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0002_auto_20181203_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('feedback_type', models.CharField(blank=True, max_length=200, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]