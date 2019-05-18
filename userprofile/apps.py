from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UserprofileConfig(AppConfig):
    name = 'userprofile'
    verbose_name = _('Userprofile')

    def ready(self):
        import userprofile.signals




