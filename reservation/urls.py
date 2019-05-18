"""reservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib import admin
from CMS import views as CMS_views
from hadmin import views as hadmin_views

from accounting import views as accounting_views
from django.conf.urls import url, include
from django.contrib import admin
from CMS import views as CMS_views
from hadmin import views as hadmin_views

urlpatterns = [
    url(r'^$', CMS_views.home, name="home"),
    url(r'^panel/', admin.site.urls),
    url(r'^admin/', include('hadmin.urls', namespace="hadmin")),
    url(r'^api/v1', include('api.urls', namespace="api")),
    url(r'^adv/', include('adv.urls', namespace="adv")),
    url(r'^posts/', include('CMS.urls', namespace="cms") ),
    url(r'^userpanel/', include('userpanel.urls', namespace="userpanel")),
    url(r'^accounting/', include('accounting.urls', namespace="accounting")),
    url(r'^tickets/', include('tickets.urls', namespace="tickets")),
    url(r'^tours/', include('tours.urls', namespace="tours")),
    url(r'^insurance/', include('insurance.urls', namespace="insurance")),
    url(r'^hotels/', include('hotels.urls', namespace="hotels")),
    url(r'^users/', include('userprofile.urls', namespace="users")),
    url(r'^master/', include('master.urls', namespace="master")),

    url(r'^accounts/list$', accounting_views.get_accounts, name="get_accounts"),
    url(r'^post/$', hadmin_views.set_article, name="set_article"),
    url(r'^post/(?P<post_id>\d+)/$', hadmin_views.edit_article, name="edit_article"),
    url(r'^post/list/$', hadmin_views.get_articles, name="get_articles"),
    url(r'^post/delete/(?P<post_id>\d+)/$', hadmin_views.delete_article, name="delete_article"),

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

    url(r'^user/edit/(?P<profile_id>\d+)/$', hadmin_views.edit_user, name="user_edit"),

    url(r'^settings$', hadmin_views.edit_settings, name="settings"),
    url(r'^$', hadmin_views.admin_login, name="admin_login"),
    url(r'^logout$', hadmin_views.admin_logout, name="admin_logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)