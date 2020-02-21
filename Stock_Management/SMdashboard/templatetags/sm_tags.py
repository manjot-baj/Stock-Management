from django import template
from django.contrib.auth.models import User
register = template.Library()


@register.filter(name='field_type')
def field_type(field):
    if not isinstance(field, dict) and field.field.widget.__class__.__name__ == 'RelatedFieldWidgetWrapper' and field.field.widget.rel.many_to_many:
        return True
    return False


@register.filter(name='is_owner')
def is_owner(user):
    if user.groups.filter(name='Owner').exists():
        return True
    return False
