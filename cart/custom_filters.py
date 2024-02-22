from django import template

register = template.Library()

@register.filter
def get_for_index(lst, index):
    return lst[index]
