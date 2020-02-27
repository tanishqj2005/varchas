from django.db import models
# from django.db.models.signals import pre_save
# from django.shortcuts import reverse
from adminportal.models import AdminProfile
# from .utils import unique_slug_generator
# from versatileimagefield.fields import VersatileImageField
from registration.models import TeamRegistration
from ckeditor_uploader.fields import RichTextUploadingField


class Event(models.Model):

    VENUE_CHOICES = (
    ('1', 'Football Ground'),
    ('2', 'Volleyball Ground'),
    ('3', 'Tennis Ground'),
    ('4', 'Badminton Ground'),
    ('5', 'Lecture Hall Complex'),
    )
    # slug = models.SlugField()
    venue = models.CharField(max_length=3, choices=VENUE_CHOICES)
    date_time = models.DateTimeField()
    event_id = models.CharField(max_length=4)
    organisers = models.ManyToManyField(AdminProfile)
    max_team_size = models.PositiveSmallIntegerField(default=1, help_text='Leave 1 for single participant event')
    about = RichTextUploadingField()

    def __str__(self):
        return self.event_id

    # def get_absolute_url(self):
    #     return reverse('events:detail', kwargs={'slug': self.slug})


# def event_pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)


# pre_save.connect(event_pre_save_receiver, sender=Event)

class Cricket(Event):
    BATTING_CHOICES = (
    ('1', 'Team 1'),
    ('2', 'Team 2'),
    )
    team1 = models.ForeignKey(TeamRegistration, on_delete=models.CASCADE, unique=False, related_name="Team1")
    team2 = models.ForeignKey(TeamRegistration, on_delete=models.CASCADE, unique=False, related_name="Team2")
    battingTeam = models.CharField(max_length=2, choices=BATTING_CHOICES)
    runs = models.IntegerField(default=0)
    wickets = models.PositiveSmallIntegerField(default=0)
    currentOver = models.PositiveSmallIntegerField(default=0)
    details = models.TextField(max_length=120, default="Cricket")
