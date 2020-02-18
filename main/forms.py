from django import forms
from .models import email


class emailForm(forms.ModelForm):
    class Meta:
        model = email
        fields = ['recipient', 'subject', 'message']
        # fields = ['subject', 'message']
