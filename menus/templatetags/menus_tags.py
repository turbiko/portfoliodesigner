from django import template

from ..models import Menu, FooterText

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    return Menu.objects.filter(slug=slug).first()

@register.simple_tag()
def get_footer(slug):
    return FooterText.objects.filter(slug=slug).first()