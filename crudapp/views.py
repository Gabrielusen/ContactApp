from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    template_name = 'crudapp/index.html'
    context_object_name = 'contact_list'

    def get_queryset(self):
        return Contact.objects.all()
