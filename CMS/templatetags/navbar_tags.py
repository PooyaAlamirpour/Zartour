#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import template
from CMS.models import Page, Product_Catagory, Catagory, Product, Article, Tag,Portfolio_tag
import jdate
import  calendar
import datetime
register = template.Library()


@register.filter
def month_name(value):
    return calendar.month_name[value]


@register.filter(name='to_price')
def to_price(price):
    formated_price = '{:,}'.format(price)
    formated_price = formated_price.replace('1', '۱').replace('0','۰').replace('2','۲').replace('3','۳').replace('4','۴').replace('5','۵').replace('6','۶').replace('7','۷').replace('8','۸').replace('9','۹')
    return formated_price


@register.filter(name='to_jalali')
def to_jalali(date):
    jd = jdate.gregorian_to_jd(date.year,date.month,date.day)
    result = jdate.jd_to_persian(jd)
    result = str(int(result[0]))+"/"+str(int(result[1]))+"/"+str(int(result[2]))
    return result


@register.filter(name='to_jalali_with_month_name')
def to_jalali_with_month_name(date):
    if isinstance(date, str) or isinstance(date, unicode) :
        yourdate = datetime.datetime.strptime(date, '%Y-%m-%d')
    else:
        yourdate = date
    jd = jdate.gregorian_to_jd(yourdate.year,yourdate.month,yourdate.day)
    result = jdate.jd_to_persian(jd)
    year = str(int(result[0]))
    month = int(result[1])
    day = str(int(result[2]))
    if month == 1:
        month = 'فروردین'
    elif month == 2:
        month = 'اردیبهشت'
    elif month == 3:
        month = 'خرداد'
    elif month == 4:
        month = 'تیر'
    elif month == 5:
        month = 'مرداد'
    elif month == 6:
        month = 'شهریور'
    elif month == 7:
        month = 'مهر'
    elif month == 8:
        month = 'آبان'
    elif month == 9:
        month = 'آذر'
    elif month == 10:
        month = 'دی'
    elif month == 11:
        month = 'بهمن'
    elif month == 12:
        month = 'اسفند'
    return day + " " + month + " ماه " + year
@register.simple_tag(name='get_url_list')
def get_url_list():
    pages = Page.objects.filter(is_in_navbar=True)
    return pages
@register.filter(name='remove_nbsp')
def remove_nbsp(value):
    value = value.replace('&nbsp;', ' ').replace('\n', ' ').replace('\r', ' ')
    while '  ' in value:
        value = value.replace('  ',' ')
    return value
@register.simple_tag(name='get_product_catagories_list')
def get_product_catagories_list():
    product_catagories = Product_Catagory.objects.filter(parent = None ).all()
    return product_catagories

@register.simple_tag(name='get_product_list')
def get_product_list():
    product_list = Product.objects.all()[0:15]
    return product_list

@register.simple_tag(name='get_article_catagories_list')
def get_article_catagories_list():
    article_catagories = Catagory.objects.all()
    return article_catagories

@register.simple_tag(name='get_article_list')
def get_article_list():
    article_list = Article.objects.all().order_by('publish_date').reverse()[0:10]
    return article_list


@register.simple_tag(name='get_last_n_article_list')
def get_last_n_list(n):
    article_list = Article.objects.all().order_by('publish_date').reverse()[0:n]
    return article_list

@register.simple_tag(name='get_article_count')
def get_article_count():
    count = Article.objects.count()
    return count



@register.simple_tag(name='get_all_tags')
def get_all_tags():
    tags = Tag.objects.all()
    return tags

@register.simple_tag(name='get_portfolio_tags')
def get_portfolio_tags():
    tags = Portfolio_tag.objects.all()
    return tags
