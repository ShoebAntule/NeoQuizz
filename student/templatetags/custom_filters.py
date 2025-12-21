from django import template
import os
from django.conf import settings

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, '')

@register.filter
def media_file_exists(value):
    if value and hasattr(value, 'name'):
        file_path = os.path.join(settings.MEDIA_ROOT, value.name)
        return os.path.exists(file_path)
    return False
