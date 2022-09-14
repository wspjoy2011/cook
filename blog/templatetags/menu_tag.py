from django import template
from django.contrib.auth import get_user_model

from blog.models import Category, Post


register = template.Library()


@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    # category = Category.objects.filter(parent__isnull=True).order_by('name')
    category = Category.objects.all()
    user = get_user_model()
    chief = user.objects.get(username='admin')
    print(chief)
    return {'list_category': category, 'chief': chief}


@register.inclusion_tag('blog/include/tags/left_menu.html')
def get_chief():
    user = get_user_model()
    chief = user.objects.get(username='admin')
    print(chief)
    return {'chief': chief}


@register.inclusion_tag('blog/include/tags/recipes_tag.html')
def get_last_posts():
    last_posts = Post.objects.select_related('category').order_by('-id')[:10]
    return {'last_posts': last_posts}


