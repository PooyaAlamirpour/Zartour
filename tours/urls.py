# api/urls.py
from django.conf.urls import url, include
from views import *
urlpatterns = [
    url(r'^$', tours, name="tours"),
    url(r'^(?P<tour_id>\d+)$', tour_details, name="details"),
]