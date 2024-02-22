from django import template

register = template.Library()

@register.filter
def get_at_index(lst, index):
    try:
        return lst[index]
    except (IndexError, TypeError):
        return None
