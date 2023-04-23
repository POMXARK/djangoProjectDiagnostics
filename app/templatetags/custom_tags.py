import os
from django import template

register = template.Library()


@register.simple_tag()
def get_host():
    return os.environ.get('REDIS_HOST') #'0.0.0.0:8000'
