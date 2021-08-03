from django import forms
from django.forms import widgets
from django.forms.widgets import TextInput, Widget

class FormContact(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your name','class':'form-control'}),
    )

    email =forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':'Your Email','class':'form-control'}),
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Subject','class':'form-control'})
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'Enter your message here','class':'form-control','rows':'6'}),
        
    )