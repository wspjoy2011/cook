from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView

from .models import Post

User = get_user_model()


class HomeView(ListView):
    model = Post
    paginate_by = 9
    context_object_name = 'posts'
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['chief'] = User.objects.get(username='admin')
        return context


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.select_related('category').select_related('author')\
            .filter(category__slug=self.kwargs.get('cat_slug'))

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['cat'] = self.kwargs.get('cat_slug')
        context['chief'] = User.objects.get(username='admin')
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['cat'] = self.kwargs.get('cat_slug')
        return context
