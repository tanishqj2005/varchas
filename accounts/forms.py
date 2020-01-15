from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import UserProfile
from registration.models import CampusAmbassador


# from nocaptcha_recaptcha.fields import NoReCaptchaField


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text', 'placeholder': ' ', 'icon': 'a'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text', 'placeholder': ' '}), required=True)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text', 'placeholder': ' '}), required=True)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'type': 'email', 'maxlength': '254', 'placeholder': ' ', 'autocomplete': 'off'}))

    password1 = forms.CharField(
        min_length=8,
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': ' '}),
        # help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Confirm Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': ' '}),
        # help_text=("Enter the same password as before, for verification."),
    )
    phone = forms.CharField(max_length=10, validators=[UserProfile.contact],
                            widget=forms.TextInput(attrs={'placeholder': ' '}))
    gender = forms.ChoiceField(choices=UserProfile.GENDER_CHOICES, required=True,
                               widget=forms.Select(attrs={'class': 'mdb-select'}))
    college = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'mdb-autocomplete', 'maxlength': '128', 'placeholder': ' '}),
        required=True)
    current_year = forms.ChoiceField(choices=UserProfile.YEAR_CHOICES, required=True,
                                     widget=forms.Select(attrs={}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'maxlength': '128'}),
                              required=True)
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'mdb-autocomplete',
                                                         'maxlength': '128', 'placeholder': ' '}), required=False)
    state = forms.ChoiceField(choices=UserProfile.STATE_CHOICES, required=True,
                              widget=forms.Select(attrs={'class': 'mdb-select'}))

    accommodation_required = forms.BooleanField(
        widget=forms.CheckboxInput(), required=False)
    referred_by = forms.CharField(
        max_length=8, required=False, widget=forms.TextInput(attrs={'placeholder': ' '}))

    # captcha = NoReCaptchaField(gtag_attrs={'data-size': 'compact'})

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

    def clean_first_name(self):
        _dict = super(RegisterForm, self).clean()
        return _dict['first_name'].capitalize()

    def clean_last_name(self):
        _dict = super(RegisterForm, self).clean()
        return _dict['last_name'].capitalize()

    def clean_email(self):
        if User.objects.filter(email__iexact=self.data['email']).exists():
            raise forms.ValidationError('This email is already registered')
        return self.data['email']

    def clean_referred_by(self):
        _referred_by = "".join(self.data['referred_by'].split()).upper()
        if self.data['referred_by'] == '':
            return None
        elif not CampusAmbassador.objects.filter(referral_code=_referred_by).exists():
            raise forms.ValidationError(
                'This is not a valid referral code, check again or leave blank')
        return CampusAmbassador.objects.get(referral_code=_referred_by)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['icon_name'] = "fa fa-id-card"
        self.fields['first_name'].widget.attrs['icon_name'] = "fa fa-user"
        self.fields['last_name'].widget.attrs['icon_name'] = "fa fa-user"
        self.fields['email'].widget.attrs['icon_name'] = "fa fa-envelope"
        self.fields['password1'].widget.attrs['icon_name'] = "fa fa-lock"
        self.fields['password2'].widget.attrs['icon_name'] = "fa fa-lock"
        self.fields['phone'].widget.attrs['icon_name'] = "fa fa-phone"
        self.fields['college'].widget.attrs['icon_name'] = "fa fa-university"
        self.fields['address'].widget.attrs['icon_name'] = "fa fa-map"
        self.fields['city'].widget.attrs['icon_name'] = "fa fa-map-marker"
        self.fields['referred_by'].widget.attrs['icon_name'] = "fa fa-id-badge"


class PasswordResetCaptchaForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': ' ', 'type': 'email', 'maxlength': '254'}))
    # captcha = NoReCaptchaField(gtag_attrs={'data-size': 'compact'})
