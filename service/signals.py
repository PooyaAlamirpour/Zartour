from django.db.models.signals import post_save
from django.dispatch import receiver
from service.models import Order
from accounting.models import *
from accounting.functions import *


@receiver(post_save, sender=Order)
def create_order_payment(sender, instance, created, **kwargs):
    if created:
        instance.payment = set_order_payment(userprofile=instance.user,amount=instance.price, text=str(instance.service))
        print "invoice created"
        instance.save()
        print "invoice saved"
