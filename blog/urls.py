from django.urls import path

from .views import (
    HomeView,
    PostListView,
    PostDetailView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:cat_slug>/', PostListView.as_view(), name='post_list'),
    path('<slug:cat_slug>/<slug:post_slug>/', PostDetailView.as_view(), name='post_detail'),
]
