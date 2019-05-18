from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from accounting import views as accounting_views

urlpatterns = [

    url(r'^accounts/list$', accounting_views.get_accounts, name="get_accounts"),
    url(r'^accounts/add$', accounting_views.set_account, name="set_account"),
    url(r'^articles/list$', accounting_views.get_articles, name="get_articles"),
    url(r'^articles/add$', accounting_views.set_article, name="set_article"),
    url(r'^payment/(?P<pk>\d+)/$$', accounting_views.PaymentDetail.as_view(), name="payment_detail"),
    url(r'^payment/confirm/(?P<confirm>\d+)/(?P<id>\d+)/$', accounting_views.confirm, name="payment_confirm"),

]