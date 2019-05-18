# -*- coding: utf-8 -*-

from django.shortcuts import render
from accounting.models import *
from accounting.functions import *
from accounting.models import *
from django.views.generic import DetailView


def get_articles(request):
    articles = AccountingArticle.objects.all().order_by('date')
    return render(
        request,
        "accounting/article/list.html",
        {
            'articles':articles,
        }
    )


def set_article(request):
    profiles = UserProfile.objects.all()
    accounts = Account.objects.all()
    if request.POST:
        pass
    return render(
        request,
        "accounting/article/add.html",
        {
            "accounts": accounts,
            "profiles":profiles,

        }
    )


def get_accounts(request):
    accounts = Account.objects.all()
    return render(
        request,
        "accounting/account/list.html",
        {
            "accounts":accounts,
        }
    )


def set_account(request):
    profiles = UserProfile.objects.all()
    accounts = Account.objects.all()
    if request.POST:
        if request.POST.get('parent'):
            parent = Account.objects.get(id=request.POST.get('parent'))
            account = parent.account_set.create(code=request.POST.get('code'), name=request.POST.get('name'))
        else:
            account = Account.objects.create(code=request.POST.get('code'), name=request.POST.get('name'))
        if request.POST.get('profile'):
            account.profile = UserProfile.objects.get(id=request.POST.get('profile'))
            account.save()
    return render(
        request,
        "accounting/account/add.html",
        {
            "accounts": accounts,
            "profiles":profiles,
        }
    )


class PaymentDetail(DetailView):
    context_object_name = 'payment'
    queryset = Payment.objects.all()
    template_name = "safarjoo/payment/invocie.html"


def confirm(request, id, confirm):
    payment = None
    try:
        payment = Payment.objects.get(id = id)
        if payment.confirm_code == confirm:
            payment.is_paid = True
            payment.save()

    finally:
        return render(
            request,
            "safarjoo/payment/invocie.html",
            {
                "payment" : payment,
            }
        )



