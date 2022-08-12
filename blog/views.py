from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.select_related('category').select_related('author').filter(category__slug=self.kwargs.get('cat_slug'))


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'


def home(request):
    return render(request, '_base.html')
