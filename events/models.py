from django.db import models
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
    EVENT_CHOICES = (
        ('1', 'Athletics'),
        ('2', 'Badminton'),
        ('3', 'Basketball'),
        ('4', 'Chess'),
        ('5', 'Cricket'),
        ('6', 'Football'),
        ('7', 'Table Tenis'),
        ('8', 'Tenis'),
        ('9', 'Volleyball'),
    )
    # slug = models.SlugField()
    event = models.CharField(max_length=2, choices=EVENT_CHOICES)
    venue = models.CharField(max_length=3, choices=VENUE_CHOICES)
    date_time = models.DateTimeField()
    time = models.DateField(null=True)
    event_id = models.CharField(max_length=4, default="NAN")
    organisers = models.ManyToManyField(AdminProfile, blank=True)
    max_team_size = models.PositiveSmallIntegerField(default=1, help_text='Leave 1 for single participant event')
    about = RichTextUploadingField()

    def __str__(self):
        return self.event_id


class Match(Event):
    team1 = models.ForeignKey(TeamRegistration, on_delete=models.CASCADE, related_name="team1")
    team2 = models.ForeignKey(TeamRegistration, on_delete=models.CASCADE, related_name="team2")
    STATUS_CHOICES = (
        ('1', 'Live'),
        ('2', 'Not Started'),
        ('3', 'Ended'),
    )
    MATCH_CHOICES = (
       ('1', 'POOL MATCH'),
       ('2', 'QUATER FINAL'),
       ('3', 'SEMI FINAL'),
       ('4', 'FINAL'),
    )
    match_type = models.CharField(max_length=2, choices=MATCH_CHOICES)
    play_status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='2')
    end_comment = models.TextField(blank=True, null=True)
    winner = models.ForeignKey(TeamRegistration, on_delete=models.CASCADE, related_name="winner", blank=True, null=True)
    final_score = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.event_id


# class Cricket(models.Model):
#     match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="match", blank=True, null=True)
#     run1 = models.IntegerField(default=0)
#     run2 = models.IntegerField(default=0)
#     wicket1 = models.IntegerField(default=0)
#     wicket2 = models.IntegerField(default=0)
#     overs1 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
#     overs2 = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

#     def score(self):
#         return [str(self.run1) + "/" + str(self.wicket1), str(self.run2) + "/" + str(self.wicket2)]


class Football(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, blank=True, null=True)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)

    def score(self):
        return [self.score1, self.score2]


class Volleyball(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, blank=True, null=True)
    score1 = models.CharField(max_length=50, null=True, default='0')
    score2 = models.CharField(max_length=50, null=True, default='0')
    setNo = models.SmallIntegerField(default=1)

    def score(self):
        return [self.score1, self.score2, self.setNo]
