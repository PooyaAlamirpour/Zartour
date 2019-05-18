from django.contrib import admin
from models import Email,EmailTemplate, SMS, SMSTemplate

# Register your models here.

admin.site.register(SMS)
admin.site.register(SMSTemplate)
