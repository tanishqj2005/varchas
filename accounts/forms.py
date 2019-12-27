from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class RegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=10, required=True)
    gender = forms.ChoiceField(choices=UserProfile.GENDER_CHOICES, required=True)
    college = forms.CharField(max_length=128)
    address = forms.CharField(max_length=128)
    state = forms.ChoiceField(choices=UserProfile.STATE_CHOICES, required=True)
    accomodation_required = forms.BooleanField()
    city = forms.CharField(max_length=32)
    no_of_days = forms.ChoiceField(choices=UserProfile.DAYS_CHOICES, required=True)
    referral = forms.CharField(widget=forms.TextInput(attrs={}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        if User.objects.filter(email__iexact=self.data['email']).exists():
            raise forms.ValidationError('This email is already registered')
        return self.data['email']

    def clean_referral(self):
        return self.data['referral'].strip().upper()
