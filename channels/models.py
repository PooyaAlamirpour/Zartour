from django.db import models
from kavenegar import KavenegarAPI, APIException, HTTPException
from django.core.mail import send_mail
from ckeditor.fields import RichTextField
from django.conf import settings


class SMSTemplate(models.Model):
    text = models.CharField(max_length=154)


class EmailTemplate(models.Model):
    text = RichTextField()


class SMSManager(models.Manager):
    def send(self, reciever, template):
        sms = self.create(reciever=reciever, smsTemplate = template)
        api = KavenegarAPI()
        sms.response = api.sms_send()

    def verify(self, reciever, code):
        sms = self.create(reciever=reciever)
        try:
            api = KavenegarAPI(settings.KAVENEGAR_API_CODE)
            params = {
                'receptor': reciever,
                'template': 'verify',
                'token': code,
                'type': 'sms',  # sms vs call
            }
            sms.response = api.verify_lookup(params)
            sms.save()

        except APIException as e:
            print(e)
        except HTTPException as e:
            print(e)

    def verify_call(self, reciever, code):
        sms = self.create(reciever=reciever)
        try:
            api = KavenegarAPI(settings.KAVENEGAR_API_CODE)
            params = {
                'receptor': reciever,
                'template': 'verify',
                'token': code,
                'type': 'call',  # sms vs call
            }
            sms.response = api.verify_lookup(params)
            sms.save()

        except APIException as e:
            print(e)
        except HTTPException as e:
            print(e)





class SMS(models.Model):
    reciever = models.CharField(max_length=11)
    smsTemplate = models.ForeignKey(SMSTemplate, blank=True, null=True)
    response = models.CharField(max_length=500, null=True, blank=True)
    objects = SMSManager()


class EmailManager(models.Model):
    def send(self, reciever, template):
        email = self.create(reciever=reciever, emailTemplate =template)
        send_mail('subject', template, 'sender@example.com',
                  [reciever, ])


class Email(models.Model):
    reciever = models.EmailField()
    emailTemplate = models.ForeignKey(EmailTemplate)
    objects = EmailManager()




