from django import forms
from django.forms import ModelForm
from .models import News, Author


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        """fiels = ('name', 'surname', 'email', 'phone_number')
        labels = {
            'name': '',
            'surname': '',
            'email': '',
            'phone_number': '',
        }"""
        fields = ('__all__')