from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Post, Comment
from .forms import CommentForm

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
        context['form'] = CommentForm()
        context['cat'] = self.kwargs.get('cat_slug')
        context['comments'] = Comment.objects.filter(post=context['post'].id)
        context['comments_count'] = Comment.objects.filter(post=context['post'].id).count()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        if form.is_valid():
            comment = Comment.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                website=form.cleaned_data['website'],
                message=form.cleaned_data['message'],
                post=self.object
            )
            comment.save()
        return HttpResponseRedirect(reverse('post_detail', args=[self.object.category.slug, self.object.slug]))


