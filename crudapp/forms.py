from django.forms import forms
from .models import Contact


class ContactForm(forms.Form):
    class meta:
        model = Contact
        fields = "__all__"
