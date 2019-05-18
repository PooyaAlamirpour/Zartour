"""shomareha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from CMS import views as CMS_views
from hadmin import views as hadmin_views
urlpatterns = [
     url(r'^$', CMS_views.home),
    url(r'^panel/', admin.site.urls),
    url(r'^admin/', include('hadmin.urls')),
    url(r'^api/v1', include('api.urls')),
    url(r'^adv/', include('adv.urls')),
    url(r'^posts/', include('CMS.urls')),
    url(r'^userpanel/', include('userpanel.urls')),
    url(r'^accounting/', include('accounting.urls')),



]
