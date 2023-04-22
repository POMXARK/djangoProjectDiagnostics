import os
from django import template

register = template.Library()


@register.simple_tag()
def get_host():
    return os.environ.get('HOST')
