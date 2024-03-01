# custum tags are defined here

from django import template

register = template.Library()

# Renders header as a component on the page, passing in the tags from parent context_dict
@register.inclusion_tag('CheeseBoardSite\header.html')
def render_header(tags):
    return {'tags': tags}