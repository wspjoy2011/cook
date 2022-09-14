from django.urls import path

from .views import ContactView, CreateContact, AboutView

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('feedback/', CreateContact.as_view(), name='feedback'),
]
