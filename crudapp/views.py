from django.forms import forms
from django.shortcuts import render, redirect
from .models import Book


def index(request):
    form = Book.objects.all()
    return render(request, '', {'form': form})
