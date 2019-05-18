from random import randint

from django.db.models.signals import post_save
from django.dispatch import receiver
from userprofile.models import UserProfile
from channels.tasks import verify_task_sms
from accounting.tasks import create_account_task


@receiver(post_save, sender=UserProfile)
def create_account(sender, instance, created, **kwargs):
    if created:
        create_account_task(instance)
        print "account created"


@receiver(post_save, sender=UserProfile)
def verify_phone(sender, instance, created, **kwargs):
    if created:
        userprofile = UserProfile.objects.get_by_natural_key(instance.username)
        if not instance.is_superuser:
            random = randint(111111, 999999)
            userprofile.set_password(random)
            userprofile.random = random
            userprofile.save()
            print "Profile Password Updated"
            verify_task_sms(userprofile)
            print "SMS Sent"
        else:
            print "NO SMS SENT TO SUPERUSER!"



