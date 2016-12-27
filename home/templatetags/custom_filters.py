from django import template

register = template.Library()


@register.filter(name='my_filter')
def my_filter(value, arg):
    return value + arg


@register.simple_tag(name='my_tag')
def my_tag():
    return 'I am a tag.'
