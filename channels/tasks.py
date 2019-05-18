from __future__ import absolute_import, unicode_literals
from celery import shared_task
from channels.models import SMS


@shared_task
def verify_task_sms(userprofile):
    SMS.objects.verify(reciever=userprofile.mobile, code=userprofile.random)


@shared_task
def verify_task_call(userprofile):
    SMS.objects.verify_call(reciever=userprofile.mobile, code=userprofile.random)




