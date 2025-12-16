from django import template

register = template.Library()


@register.filter(name="sub")
def alaki(value, a:str):
    k = a.split("|")
    s = sum([int(i) for i in k])
    return value-s