from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView

from .models import ContactLink, About
from .forms import ContactForm


class ContactView(View):
    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ContactForm()
        context = {
            'contacts': contacts,
            'form': form,
        }
        return render(request, 'contact/contact.html', context)


class CreateContact(CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('home')


class AboutView(View):
    def get(self, request):
        about = About.objects.last()
        context = {
            'about': about,
        }
        return render(request, 'contact/about.html', context)

