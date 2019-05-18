from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from .views import adv_form, adv_item, search
urlpatterns = [

    url(r'^new$', adv_form, name="adv_form"),
    url(r'^search$', search, name="search"),
    url(r'^2$', adv_item, name="adv_item"),
]