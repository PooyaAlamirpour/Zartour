from django.shortcuts import render
from django.contrib.auth import authenticate,  login, logout
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response

from userprofile.models import UserProfile, User, Subscriber
#from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from random import randint
#from sms.kavenegar import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import requests
from django.conf import settings
import json
from django.core.urlresolvers import reverse_lazy


from rest_framework import generics, status

from . import models
from . import serializers


class UserListView(generics.ListCreateAPIView):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserSerializer

    def create(self, request, *args, **kwargs):
        myModel, created = UserProfile.objects.update_or_create(
            mobile=request.data['mobile'],
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
        )

        # require context={'request': request} because i'm using HyperlinkModelSerializer
        serializer = serializers.UserSerializer(myModel, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()

        if created:
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            myModel.send_verify_code()
            return Response(serializer.data, status.HTTP_200_OK)

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@csrf_exempt
def delete_address(request):
    address_id = int(request.POST.get('id'))
    address = Address.objects.get(pk=address_id)
    if request.user.is_authenticated:
        profile = UserProfile.objects.get_profile(request.user)
        if address.profile == profile:
            address.delete()
            return JsonResponse({
                'status': 'success'
            })
    return JsonResponse({
        'status': 'failed'
    })


@csrf_exempt
def edit_address(request):
    address_id = int(request.POST.get('addressId'))
    address = Address.objects.get(pk=address_id)
    serialized_address = serializers.serialize('json', [address, ])
    response = JsonResponse(
        {
            'id':address.id,
            'name':address.name,
            'address':address.address,
            'phone':address.phone,
            'mobile':address.mobile,
            'postal_code':address.postal_code,
            'city': address.city,
            'province':address.province
        }
    )
    print response
    return response


def register(request):
    next_url = request.GET.get('next')
    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        postal_code = request.POST.get('postal_code')
        user = User.objects.create_user(username=username, password=password)
        UserProfile.objects.create(user=user, mobile=mobile, default_address=address, is_ordinary_user=True, postal_code=postal_code)
        if user:
            if user.is_active:
                login(request, user)
                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return HttpResponseRedirect(reverse('home'))
    return render(
        request,
        'safarjoo/user/register.html',
        {

        })


def register_step1(request):
    next_url = request.GET.get('next')
    valid = True
    if request.POST:
        mobile = request.POST.get('mobile')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        users = UserProfile.objects.filter(mobile=mobile)
        if users.count() > 0:
            users[0].send_verify_code()
        else:
            user = UserProfile.objects.create(mobile=mobile, first_name=first_name, last_name=last_name)
        return render(
            request,
            'bilit360/user/verify.html',
            {
                'mobile': mobile,
            })
    valid = False
    return render(
        request,
        'bilit360/user/login.html',
        {
            "status": valid,
        }
    )


@login_required
def register_stepN(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except:
        profile = None
    if profile:
        return HttpResponseRedirect('/profile/')
    else:
        try:
            if request.method == 'POST':
                request.POST._mutable = True
                request.POST['dob'] = request.POST['dob'].replace("/", "-")
        except:
            pass
        return render(
            request,
            'user/register_step2.html',
            {

            }
        )


def user_login(request):
    next_url = request.GET.get('next')
    if request.user.is_authenticated():
        if next_url:
            return HttpResponseRedirect(next_url)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print username
        print password
        if user:
            if user.is_active:
                login(request, user)
                print next_url
                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your User is inactive")
        else:
            return HttpResponse("Invalid login details")
    else:
        return HttpResponseRedirect(reverse('home'))


def user_login_step1(request):
    NOT_REGISTERED_ERROR = False
    if request.POST:
        mobile = request.POST['mobile']
        users = UserProfile.objects.filter(username=mobile)
        if users.count()>0:
            users[0].send_verify_code()
            return render(
                request,
                'bilit360/user/verify.html',
                {
                    'mobile': mobile,
                })
        else:
            NOT_REGISTERED_ERROR = True
    return render(
        request,
        'bilit360/user/login.html',
        {
           'NOT_REGISTERED_ERROR': NOT_REGISTERED_ERROR
        })

def verify_using_call(request, mobile):
    user = UserProfile.objects.get(username=mobile)
    user.call_verify_code()
    return render(
        request,
        'bilit360/user/verify.html',
        {
            'mobile': mobile,
        })



def user_login2(request):
    next_url = request.GET.get('next')
    if request.user.is_authenticated():
        if next_url:
            return HttpResponseRedirect(next_url)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print username
        print password
        if user:
            if user.is_active:
                login(request, user)
                print next_url
                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your User is inactive")
        else:
            return HttpResponse("Invalid login details")
    else:
        return render(
            request,
            'safarjoo/user/login.html',
            {

            })


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def timeline(request):
    queries = {}
    filters = {}
    if 'gender' in request.GET:
        if request.GET['gender'] == '0':
            queries['gender'] = False
            gender = False
        if request.GET['gender'] == '1':
            queries['gender'] = True
            gender = True





    for k, v in queries.items():
        if v != None:
            filters[k] = v
    profiles = UserProfile.objects.filter(**filters)
    if 'age-max' in request.GET:
        if is_int(request.GET['age-max']):
            age_max = int(request.GET['age-max'])
            today = datetime.datetime.now()
            max_birthdate = datetime.datetime(today.year - age_max - 1, today.month, today.day)
            profiles = profiles.filter(dob__gte = max_birthdate)

    if 'age-min' in request.GET:
        if is_int(request.GET['age-min']):
            age_min = int(request.GET['age-min'])
            today = datetime.datetime.now()
            min_birthdate = datetime.datetime(today.year - age_min, today.month, today.day)
            profiles = profiles.filter(dob__lte = min_birthdate)


    return render(
        request,
        'profile/timeline.html',
        {
            'user':request.user,
            'profiles':profiles,
        }
    )



@login_required
def edit_profile(request):
    if request.method == 'POST':
        #update profile
        #request.POST._mutable = True
        #request.POST['dob'] = request.POST['dob'].replace("/", "-")
        profile = UserProfile.objects.get(user=request.user)
        #profile.dob = request.POST['dob']
        profile.user.first_name = request.POST['first_name']
        profile.user.last_name = request.POST['last_name']
        #profile.gender = request.POST['gender']
        profile.mobile = request.POST.get('mobile_number')
        profile.phone = request.POST.get('phone')
        profile.address = request.POST.get('address')
        if request.POST.get('gender') =='0':
            profile.gender = False
        elif request.POST.get('gender') =='1':
            profile.gender = True
       # profile.city = City.objects.get(id=request.POST.get('city'))
        profile.save()
        profile.user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def save_avatar(request):
    if request.method == 'POST':
        profile = UserProfile.objects.get(user=request.user)
        profile.avatar = request.FILES.get('avatar')
        profile.save()
        profile.user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def show_profile(request, user_id):
    user_id = int(user_id)
    profile = UserProfile.objects.get(user_id=user_id)
    return render(
        request,
        'profile/show_profile.html',
        {
            'profile': profile
        }
    )


def subscribe(request):
    if request.POST:
        first_name = None
        last_name = None
        mobile = None
        is_domestic = 1
        if 'first_name' in request.POST:
            first_name = request.POST['first_name']
        if 'last_name' in request.POST:
            last_name = request.POST['last_name']
        if 'mobile' in request.POST:
            mobile = request.POST['mobile']
        if 'is_domestic' in request.POST:
            is_domestic = request.POST['is_domestic']
        if is_domestic == '0':
            is_domestic = True
        else:
            is_domestic = False
        print is_domestic
        Subscriber.objects.create(first_name=first_name, last_name=last_name, mobile=mobile, domestic_tour=is_domestic, subscription_date = datetime.datetime.now())

        return HttpResponseRedirect(reverse('home'))
