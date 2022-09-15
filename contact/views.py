from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView

from .models import ContactLink, About
from .forms import ContactForm

User = get_user_model()


class ContactView(View):
    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ContactForm()
        chief = User.objects.get(username='admin')
        context = {
            'contacts': contacts,
            'form': form,
            'chief': chief
        }
        return render(request, 'contact/contact.html', context)


class CreateContact(CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('home')


class AboutView(View):
    def get(self, request):
        about = About.objects.last()
        chief = User.objects.get(username='admin')
        context = {
            'about': about,
            'chief': chief
        }
        return render(request, 'contact/about.html', context)

