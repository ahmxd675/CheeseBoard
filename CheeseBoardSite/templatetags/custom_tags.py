# custum tags are defined here

from django import template

register = template.Library()

# Renders header as a component on the page, passing in the tags from parent context_dict
@register.inclusion_tag('CheeseBoardSite\header.html')
def render_header(tags):
    return {'tags': tags}

# Renders the grid showing all the posts
@register.inclusion_tag('CheeseBoardSite\post_grid.html')
def render_post_grid(posts):
    return {'posts': posts}

# Renders a single post
@register.inclusion_tag('CheeseBoardSite\post_card.html')
def render_post(post):
    return {'post': post}