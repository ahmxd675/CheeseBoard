from django import template

register = template.Library()

@register.inclusion_tag('CheeseBoardSite\header.html')
def render_header(tags):
    return {'tags': tags}