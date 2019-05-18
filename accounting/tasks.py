from __future__ import absolute_import, unicode_literals
from celery import shared_task
from accounting.models import Account



@shared_task
def create_account_task(userprofile):
    Account.objects.create_account(userprofile=userprofile)



