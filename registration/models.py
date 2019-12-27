from django.db.models.signals import pre_save
from django.db import models
from .utils import unique_ca_referral_code
from django.core.validators import RegexValidator
from accounts.models import UserProfile
from events.models import Event


class CampusAmbassador(models.Model):
    YEAR_CHOICES = (
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year'),
        ('5', 'Fifth Year'),
    )
    # Validators
    contact = RegexValidator(r'^[0-9]{10}$', message='Not a valid number!')
    # Model
    name = models.CharField(max_length=32)
    email = models.EmailField()
    college = models.CharField(max_length=128)
    current_year = models.CharField(max_length=1, choices=YEAR_CHOICES)
    address = models.CharField(max_length=128)
    phone = models.CharField(max_length=10, validators=[contact])
    fb_link = models.URLField()
    publicize_varchas = models.TextField(max_length=512)
    past_experience = models.TextField(max_length=512)
    referral_code = models.CharField(max_length=7, editable=False)

    def __str__(self):
        return self.name


def pre_save_campus_ambassador(sender, instance, **kwargs):
    if instance._state.adding is True:
        instance.referral_code = unique_ca_referral_code(instance)


pre_save.connect(pre_save_campus_ambassador, sender=CampusAmbassador)


class EventRegistration(models.Model):
    participant = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return "{leader} - {event}".format(leader=self.participant, event=self.event)


class TeamRegistration(EventRegistration):
    members = models.ManyToManyField(UserProfile)
