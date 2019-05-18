from django import template
from CMS.models import Setting
register = template.Library()

@register.simple_tag(name='get_settings')
def get_url_list():
    settings = Setting.objects.get(is_active = True)
    return settings