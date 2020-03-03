from django import forms
from .models import email


class emailForm(forms.ModelForm):
    class Meta:
        model = email
        fields = ['recipient', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'cols': 95, 'rows': 10}),
        }
