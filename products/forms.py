from django import forms
from .models import Email


class AddEmailForm(forms.Form):
    email = forms.EmailField()
    
