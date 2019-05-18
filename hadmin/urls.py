# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from accounting import views as accounting_views
from django.conf.urls import url, include
from django.contrib import admin
from CMS import views as CMS_views
from hadmin import views as hadmin_views
urlpatterns = [

    url(r'^flight/list$', hadmin_views.TicketListView.as_view(), name="get_flights"),
    url(r'^flight/excel$', hadmin_views.flights_excel, name="flight_excel"),



    url(r'^accounts/list$', accounting_views.get_accounts, name="get_accounts"),

    url(r'^subscribers$', hadmin_views.subscriber_list, name="subscriber_list"),
    url(r'^subscribers/excel$', hadmin_views.subscriber_excel, name="subscriber_excel"),

    url(r'^userlist$', hadmin_views.user_list, name="user_list"),
    url(r'^feedbacks/list$', hadmin_views.feedback_list, name="feedback_list"),
    url(r'^feedbacks/delete/(?P<feedback_id>\d+)/$', hadmin_views.feedback_delete, name="feedback_delete"),

    url(r'^post/$', hadmin_views.set_article, name="set_article"),
    url(r'^post/(?P<post_id>\d+)/$', hadmin_views.edit_article, name="edit_article"),
    url(r'^post/list/$', hadmin_views.get_articles, name="get_articles"),
    url(r'^post/delete/(?P<post_id>\d+)/$', hadmin_views.delete_article, name="delete_article"),

    url(r'^hotels/$', hadmin_views.set_hotel, name="set_hotel"),
    url(r'^hotels/(?P<hotel_id>\d+)/$', hadmin_views.edit_hotel, name="edit_hotel"),
    url(r'^hotels/list/$', hadmin_views.get_hotels, name="get_hotels"),
    url(r'^hotels/delete/(?P<hotel_id>\d+)/$', hadmin_views.delete_hotel, name="delete_hotel"),

    url(r'^hotels/options/list/$', hadmin_views.get_options, name="get_options"),
    url(r'^hotels/options/delete/(?P<option_id>\d+)/$', hadmin_views.delete_option, name="delete_option"),

    url(r'^tours/(?P<tour_id>\d+)/hotels/add/$', hadmin_views.set_hotel_tour, name="set_hotel_tour"),
    url(r'^tours/(?P<tour_id>\d+)/hotels/delete/(?P<hotel_id>\d+)$', hadmin_views.delete_hotel_tour, name="delete_hotel_tour"),
    url(r'^tours/(?P<tour_id>\d+)/hotels/edit/(?P<hotel_id>\d+)$', hadmin_views.edit_hotel_tour, name="edit_hotel_tour"),

    url(r'^tours/services/list/$', hadmin_views.get_services, name="get_services"),
    url(r'^tours/services/delete/(?P<service_id>\d+)/$', hadmin_views.delete_service, name="delete_service"),

    url(r'^tours/$', hadmin_views.set_tour, name="set_tour"),
    url(r'^tours/(?P<tour_id>\d+)/$', hadmin_views.edit_tour, name="edit_tour"),
    url(r'^tours/list/$', hadmin_views.get_tours, name="get_tours"),
    url(r'^tours/delete/(?P<tour_id>\d+)/$', hadmin_views.delete_tour, name="delete_tour"),

    url(r'^city/list/(?P<country_id>\d+)/$', hadmin_views.get_cities, name="get_cities"),
    url(r'^city/delete/(?P<city_id>\d+)/$', hadmin_views.delete_city, name="delete_city"),

    url(r'^country/list/$', hadmin_views.get_countries, name="get_countries"),
    url(r'^country/delete/(?P<country_id>\d+)/$', hadmin_views.delete_country, name="delete_country"),

    url(r'^airline/list/$', hadmin_views.get_airlines, name="get_airlines"),
    url(r'^airline/delete/(?P<airline_id>\d+)/$', hadmin_views.delete_airline, name="delete_airline"),


    url(r'^project/$', hadmin_views.set_project, name="set_project"),
    url(r'^project/(?P<post_id>\d+)/$', hadmin_views.edit_project, name="edit_project"),
    url(r'^project/list/$', hadmin_views.get_projects, name="get_projects"),
    url(r'^project/delete/(?P<post_id>\d+)/$', hadmin_views.delete_project, name="delete_project"),


    url(r'^page/$', hadmin_views.set_page, name="set_page"),
    url(r'^page/(?P<page_id>\d+)/$', hadmin_views.edit_page, name="edit_page"),
    url(r'^page/list/$', hadmin_views.get_pages, name="get_pages"),
    url(r'^page/delete/(?P<page_id>\d+)/$', hadmin_views.delete_page, name="delete_page"),

    url(r'^comment/list/$', hadmin_views.get_comments, name="get_comments"),
    url(r'^comment/delete/(?P<comment_id>\d+)/$', hadmin_views.delete_comment, name="delete_comment"),

    url(r'^tag/list/$', hadmin_views.get_tags, name="get_tags"),
    url(r'^tag/delete/(?P<tag_id>\d+)/$', hadmin_views.delete_tag, name="delete_tag"),

    url(r'^cat/list/$', hadmin_views.get_cats, name="get_cats"),
    url(r'^cat/delete/(?P<cat_id>\d+)/$', hadmin_views.delete_cat, name="delete_cat"),

    url(r'^slider/$', hadmin_views.set_slider, name="set_slider"),
    url(r'^slider/(?P<slider_id>\d+)/$', hadmin_views.edit_slider, name="edit_slider"),
    url(r'^slider/delete/(?P<slider_id>\d+)/$', hadmin_views.delete_slider, name="delete_slider"),
    url(r'^slider/list/$', hadmin_views.get_sliders, name="get_sliders"),

    url(r'^product/$', hadmin_views.set_product, name="set_product"),
    url(r'^product/(?P<product_id>\d+)/$', hadmin_views.edit_product, name="edit_product"),
    url(r'^product/delete/(?P<product_id>\d+)/$', hadmin_views.delete_product, name="delete_product"),
    url(r'^product/list/$', hadmin_views.get_products, name="get_products"),

    url(r'^edit/charity$', hadmin_views.edit_charity, name="edit_charity"),
    url(r'^edit/about$', hadmin_views.edit_about, name="edit_about"),
    url(r'^edit/contact$', hadmin_views.edit_contact, name="edit_contact"),


    url(r'^userlist$', hadmin_views.user_list, name="user_list"),
    url(r'^user/edit/(?P<profile_id>\d+)/$', hadmin_views.edit_user, name="user_edit"),
    url(r'^user/excel$', hadmin_views.users_excel, name="users_excel"),



    url(r'^settings$', hadmin_views.edit_settings, name="settings"),
    url(r'^$', hadmin_views.admin_login, name="admin_login"),
    url(r'^logout$', hadmin_views.admin_logout, name="admin_logout"),
]