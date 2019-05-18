# api/urls.py
from django.conf.urls import url, include
from api.views import AirportDetail, AirportList

urlpatterns = [
    url(r'^/users/', include('userprofile.urls',namespace="users")),
    url(r'^/rest-auth/', include('rest_auth.urls')),
    url(r'^/data/airports/(?P<pk>[\w\-]+)/$', AirportDetail.as_view(), name='airport_detail'),
    url(r'^/data/airports$', AirportList.as_view(), name='airport_list'),
]