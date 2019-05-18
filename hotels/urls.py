# hotels/urls.py
from django.conf.urls import url, include
from views import *
urlpatterns = [
    url(r'^$', hotels, name="hotels"),
    url(r'^(?P<hotel_id>\d+)$', hotel_details, name="details"),
    url(r'^cities/(?P<country_id>\d+)$', city_list, name="city_list"),
]