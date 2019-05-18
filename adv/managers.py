from django.db import models

class AdvManager(models.Manager):

    def confirm(self, adv):
        adv = self.get(id = adv.id)
        adv.is_confirmed = true
        adv.save()
