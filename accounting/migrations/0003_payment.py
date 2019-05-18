# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-27 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_account_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField(default=0)),
                ('creation_date', models.DateField(blank=True, null=True)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('confirm_code', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
