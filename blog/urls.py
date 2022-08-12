from django.urls import path

from .views import (
    home,
    PostListView,
    PostDetailView
)

urlpatterns = [
    path('', home, name='home'),
    path('<slug:cat_slug>/', PostListView.as_view(), name='post_list'),
    path('<slug:cat_slug>/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

]
