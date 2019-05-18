# hotels/urls.py
from django.conf.urls import url, include
from views import *
urlpatterns = [
    url(r'^cities/(?P<country_id>\d+)$', city_list, name="city_list"),
]