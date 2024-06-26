from django import template
from django.utils.safestring import mark_safe
import markdown


register = template.Library()

@register.filter
def sub(value,arg):
    print(value, arg)
    return value - arg

@register.filter()
def mark(value):
    extensions = ["nl2br", "fensed_code"]
    return mark_safe(markdown(value, extensions = extensions))

