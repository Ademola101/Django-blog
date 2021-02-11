from django import template
from ..models import BlogPost

register = template.Library()

@register.simple_tag()
def total_posts():
    return BlogPost.body.count()