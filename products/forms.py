from django import forms
from .models import Email


class AddEmailForm(forms.ModelForm):
    
    class Meta:
        model = Email
        fields = ('email',)
    
