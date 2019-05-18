from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ServiceConfig(AppConfig):
    name = 'service'
    verbose_name = _('services')

    def ready(self):
        import service.signals

