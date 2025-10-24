from django import template

register = template.Library()

@register.filter
def get_field(form, field_name):
    """Return form field by variable name."""
    return form[field_name]
