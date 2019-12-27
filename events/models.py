from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from django.shortcuts import reverse
from adminportal.models import AdminProfile
from .utils import unique_slug_generator
# from versatileimagefield.fields import VersatileImageField
from ckeditor_uploader.fields import RichTextUploadingField


class Event(models.Model):
    ETYPE_CHOICES = (
        ('1', 'Sporting Event'),
        ('2', 'Informal Event'),
    )
    name = models.CharField(max_length=32)
    slug = models.SlugField()
    e_type = models.CharField(max_length=1, choices=ETYPE_CHOICES)
    venue = models.CharField(max_length=3, choices=settings.VENUE_CHOICES)
    date_time = models.DateTimeField()
    event_id = models.CharField(max_length=4)
    # cover = VersatileImageField(upload_to='event')
    organisers = models.ManyToManyField(AdminProfile)
    max_team_size = models.PositiveSmallIntegerField(default=1, help_text='Leave 1 for single participant event')
    about = RichTextUploadingField()
    details = RichTextUploadingField()
    custom_html = models.TextField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('events:detail', kwargs={'slug': self.slug})


def event_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(event_pre_save_receiver, sender=Event)
