from django.db.models.signals import post_save
from django.dispatch import receiver
from adv.models import Adv


@receiver(post_save, sender=Adv)
def channels_trigger(sender, instance, created, **kwargs):
    if created:
        if sender.is_confirmed:
            print "sms + email verified"
        else:
            print "sms + email unverified"
