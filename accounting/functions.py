from models import *
import datetime as dt
from django.db.models import Q
from datetime import datetime


def set_article(amount, debit, credit, text=None, date=dt.datetime.now()):
    return AccountingArticle.objects.create(amount=amount, debit=debit, credit=credit, text=text, date=date)


def get_balance(account):
    return AccountingArticle.objects.filter(Q(debit=account) | Q(credit=account)).order_by('date')


def get_balance_table_by_profile(profile):
    account = Account.objects.get(profile=profile)
    return get_balance(account)


def get_balance_amount_by_profile(profile):
    account = Account.objects.get(profile=profile)
    credit = 0
    for article in account.credits:
        credit = credit + article.amount
    for article in account.debits:
        credit = credit - article.amount
    return credit


def withdraw(userprofile, amount, creditor, text=None, date=datetime.now()):
    account = Account.objects.get(profile = userprofile)
    set_article(amount, debit=account, credit=creditor, text="withdraw"+":"+text, date=date)


def deposit(userprofile, amount, debitor, text=None, date=datetime.now()):
    account = Account.objects.get(profile = userprofile)
    set_article(amount, debit=debitor, credit=account , text="withdraw"+":"+text, date=date)


def set_order_payment(userprofile, amount, text=None, date=datetime.now()):
    main_account = Account.objects.get(code="Main")
    account = Account.objects.get(profile = userprofile)
    set_article(amount, debit=account, credit=main_account , text="order"+":"+text, date=date)

