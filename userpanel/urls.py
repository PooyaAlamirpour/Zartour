from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from userpanel import views as userpanel_views

urlpatterns = [

    url(r'^profile$', userpanel_views.profile, name="profile"),

]