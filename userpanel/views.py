# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from userprofile.models import UserProfile
# Create your views here.


def profile(request):
    me = UserProfile.objects.get(username=request.user.username)
    if request.POST:
        me.first_name = request.POST.get('first_name')
        me.last_name = request.POST.get('last_name')
        me.phone = request.POST.get('phone')
        me.code_meli = request.POST.get('code_meli')
        me.postal_code = request.POST.get('postal_code')
        me.email = request.POST.get('email')
        me.save()
    return render(
        request = request,
        template_name="bilit360/userpanel/userpanel.html",
        context={ 'profile': me,}
    )