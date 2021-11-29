from django import template
from ..models import blog_post


register = template.Library()


@register.simple_tag
def count_blogs():
    all_blogs = blog_post.objects.all().count()
    return all_blogs