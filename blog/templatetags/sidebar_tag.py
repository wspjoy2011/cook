from django import template

from blog.models import Post, Category


register = template.Library()


@register.simple_tag()
def get_posts():
    """Get first five records from Post"""
    posts_side = Post.objects.all()[:5]
    return posts_side


@register.simple_tag()
def get_first_post():
    """Get first record from Post"""
    first = Post.objects.all().last()
    return first


@register.simple_tag()
def get_categories():
    """Get all records from Category"""
    category = Category.objects.all()
    return category

