from django import forms



class AddEmail(forms.Form):
    email = forms.EmailField()