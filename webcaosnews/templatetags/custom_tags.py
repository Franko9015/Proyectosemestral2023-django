from django import template

register = template.Library()

@register.filter
def get_user_roles(user):
    return [group.name.lower() for group in user.groups.all()]
