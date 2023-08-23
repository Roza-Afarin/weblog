from django import template
from blog.models import post

register = template.Library()

@register.inclusion_tag('website/latest-posts.html')
def recentposts(arg=2):
    posts = post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}