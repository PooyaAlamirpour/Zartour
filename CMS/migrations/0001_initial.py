# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-03 09:23
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField()),
                ('publish_date', models.DateTimeField()),
                ('title', models.CharField(max_length=150)),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('slug', models.CharField(max_length=150)),
                ('image_alt', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=300)),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('icon', models.ImageField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Catagory',
                'verbose_name_plural': 'Catagories',
            },
        ),
        migrations.CreateModel(
            name='CharityPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('donated_amount', models.BigIntegerField(blank=True, null=True)),
                ('charity_title1', models.CharField(blank=True, max_length=200, null=True)),
                ('charity_text1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('charity_image1', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('charity_title2', models.CharField(blank=True, max_length=200, null=True)),
                ('charity_text2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('charity_image2', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('charity_title3', models.CharField(blank=True, max_length=200, null=True)),
                ('charity_text3', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('charity_image3', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('charity_title4', models.CharField(blank=True, max_length=200, null=True)),
                ('charity_text4', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('charity_image4', models.ImageField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('commenter', models.CharField(blank=True, max_length=100, null=True)),
                ('commenter_email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('commenter_website', models.URLField(blank=True, default=None, null=True)),
                ('comment_date', models.DateTimeField(blank=True, null=True)),
                ('reply', models.CharField(blank=True, max_length=300, null=True)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('content', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='FAQCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to=b'')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField()),
                ('publish_date', models.DateTimeField()),
                ('title', models.CharField(max_length=80)),
                ('is_in_navbar', models.BooleanField(verbose_name='Has a menu link')),
                ('navbar_name', models.CharField(max_length=50)),
                ('link_address', models.CharField(max_length=50)),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('description_title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('image_alt', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=150)),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('image_alt', models.CharField(blank=True, max_length=150, null=True)),
                ('catagory', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='CMS.Portfolio_category')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=60)),
                ('slug', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('icon', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('image', models.ImageField(upload_to=b'')),
                ('image_alt', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=70, null=True)),
                ('slug', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('icon', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('description_title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.CharField(max_length=50)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='CMS.Product_Catagory')),
            ],
            options={
                'verbose_name': 'Product Catagory',
                'verbose_name_plural': 'Product Catagories',
            },
        ),
        migrations.CreateModel(
            name='ProductAlternativeName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alternative_name', models.CharField(max_length=100)),
                ('lang_code', models.CharField(max_length=3)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMS.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField()),
                ('publish_date', models.DateTimeField()),
                ('title', models.CharField(max_length=150)),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('slug', models.CharField(max_length=150)),
                ('image_alt', models.CharField(blank=True, max_length=150, null=True)),
                ('catagory', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='CMS.Catagory')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='QandA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer', ckeditor.fields.RichTextField()),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMS.FAQCatagory')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=300)),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('icon', models.ImageField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('website_icon', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('website_logo', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('website_name', models.CharField(max_length=100)),
                ('website_slogan', models.CharField(blank=True, max_length=500, null=True)),
                ('brief_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('long_descriptioon', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('address_line_1', models.CharField(blank=True, max_length=200, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=200, null=True)),
                ('info_email', models.EmailField(max_length=254)),
                ('fax_number', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number_1', models.CharField(max_length=20)),
                ('phone_number_2', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number_3', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number_4', models.CharField(blank=True, max_length=20, null=True)),
                ('header_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('googlemap_lan', models.CharField(blank=True, max_length=50, null=True)),
                ('googlemap_lat', models.CharField(blank=True, max_length=50, null=True)),
                ('facebook_link', models.CharField(blank=True, max_length=100, null=True)),
                ('gplus_link', models.CharField(blank=True, max_length=100, null=True)),
                ('telegram_link', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Settings',
                'verbose_name_plural': 'Settings',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.IntegerField()),
                ('image', models.ImageField(upload_to=b'')),
                ('caption', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charity', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=60)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin_link', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook_link', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='CMS.Tag'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_catagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMS.Product_Catagory'),
        ),
        migrations.AddField(
            model_name='portfolio_item',
            name='tags',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='CMS.Portfolio_tag'),
        ),
        migrations.AddField(
            model_name='portfolio_image',
            name='portfolio_item',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='CMS.Portfolio_item'),
        ),
    ]