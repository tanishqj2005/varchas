from django.db import models
from django.contrib.auth.models import User
from events.models import Event


# from .utils import unique_rg_number
# from django.db.models.signals import pre_save


class UserProfile(models.Model):
    # choices
    ACCOMMODATION_CHOICES = (
        ('N', 'No'),
        ('Y', 'Yes'),
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender'),
    )
    DAYS_CHOICES = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
    )
    STATE_CHOICES = (
        ('1', 'Andhra Pradesh'),
        ('2', 'Arunachal Pradesh'),
        ('3', 'Assam'),
        ('4', 'Bihar'),
        ('5', 'Chhattisgarh'),
        ('6', 'Goa'),
        ('7', 'Gujarat'),
        ('8', 'Haryana'),
        ('9', 'Himachal Pradesh'),
        ('10', 'Jammu & Kashmir'),
        ('11', 'Jharkhand'),
        ('12', 'Karnataka'),
        ('13', 'Kerala'),
        ('14', 'Madhya Pradesh'),
        ('15', 'Maharashtra'),
        ('16', 'Manipur'),
        ('17', 'Meghalaya'),
        ('18', 'Mizoram'),
        ('19', 'Nagaland'),
        ('20', 'Odisha'),
        ('21', 'Punjab'),
        ('22', 'Rajasthan'),
        ('23', 'Sikkim'),
        ('24', 'Tamil Nadu'),
        ('25', 'Telangana'),
        ('26', 'Tripura'),
        ('27', 'Uttarakhand'),
        ('28', 'Uttar Pradesh'),
        ('29', 'West Bengal'),
        ('30', 'Andaman & Nicobar Islands'),
        ('31', 'Delhi'),
        ('32', 'Chandigarh'),
        ('33', 'Dadra & Naagar Haveli'),
        ('34', 'Daman & Diu'),
        ('35', 'Lakshadweep'),
        ('36', 'Puducherry'),
    )
    # Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default='M')
    college = models.CharField(max_length=128)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    accommodation_required = models.CharField(max_length=1, choices=ACCOMMODATION_CHOICES, blank=True)
    accomodation_type = models.CharField(max_length=1, default=1)
    amount_required = models.PositiveSmallIntegerField(default=0, blank=True)
    amount_paid = models.PositiveSmallIntegerField(default=0, blank=True)
    no_of_days = models.CharField(max_length=1, choices=DAYS_CHOICES)
    referral = models.CharField(max_length=7, blank=True, null=True)
    id_issued = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to='qr_code', blank=True, null=True)
    events_registered = models.ManyToManyField(Event, blank=True)
    teamId = models.CharField(max_length=15, default="NULL")

    def __str__(self):
        return self.user.username
