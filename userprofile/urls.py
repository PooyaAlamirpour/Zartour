from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from userprofile import views as userprofile_views

urlpatterns = [
    url(r'^$', userprofile_views.UserListView.as_view(), name="users"),
    # url(r'^register/step1$', userprofile_views.register_step1, name="register_step1"),
    # url(r'^confirm$', userprofile_views.confirm, name="confirm"),

    url(r'^register$', userprofile_views.register_step1, name="register"),
    url(r'^verify$', userprofile_views.user_login, name="verify"),
    url(r'^verify/(?P<mobile>[\w\-]+)/$', userprofile_views.verify_using_call, name="verify_using_call"),
    url(r'^login$', userprofile_views.user_login_step1, name="login"),
    url(r'^logout$', userprofile_views.user_logout, name="logout"),
    url(r'^subscribe$', userprofile_views.subscribe, name="subscribe"),
    #url(r'^user/login$', userprofile_views.set_account, name="set_account"),

]