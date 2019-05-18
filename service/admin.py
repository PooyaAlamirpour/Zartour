from django.contrib import admin
from models import Order, JustOneOtherPanelService, JustOneOtherPanelCategory, JustOneOtherPanelType
# Register your models here.
admin.site.register(JustOneOtherPanelCategory)
admin.site.register(JustOneOtherPanelType)
admin.site.register(JustOneOtherPanelService)
admin.site.register(Order)