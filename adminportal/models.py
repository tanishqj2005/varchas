from django.db import models
from django.contrib.auth.models import User
# from versatileimagefield.fields import VersatileImageField
from django.core.validators import RegexValidator


class AdminProfile(models.Model):
    # Validators
    contact = RegexValidator(r'^[0-9]{10}$', message='Not a valid number!')
    # Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, validators=[contact])
    # avatar = VersatileImageField(upload_to='avatar', blank=True, null=True)
