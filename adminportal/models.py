from django.db import models
from django.contrib.auth.models import User
# from versatileimagefield.fields import VersatileImageField
from django.core.validators import RegexValidator


class AdminProfile(models.Model):
    DEPARTMENT_CHOICES = (
        ('NONE', 'None'),
        ('FLAG', 'Flagship'),
        ('ONL9', 'Online'),
        ('PUBR', 'Public Relations'),
        ('MAR', 'Marketing'),
        ('EVNT', 'Sports Events'),
    )
    # Validators
    contact = RegexValidator(r'^[0-9]{10}$', message='Not a valid number!')
    # Model
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True},
                                verbose_name='username')
    phone = models.CharField(max_length=10, validators=[contact])
    # avatar = VersatileImageField(upload_to='avatar')
    department = models.CharField(choices=DEPARTMENT_CHOICES, default='NONE', max_length=8)

    def __str__(self):
        return self.user.username

    @property
    def name(self):
        return self.user.get_full_name()

    # def avatar_thumbnail(self):
    #     return mark_safe(
    #         '<img src="{src}" style="width: 100px; height: 100" />'.format(src=self.avatar.crop['100x100'].url))
    #
    # avatar_thumbnail.short_description = 'avatar'
    # avatar_thumbnail.allow_tags = True


class DepartmentTeam(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(AdminProfile, through='DepartmentTeamMembership',
                                     through_fields=('department_team', 'profile'))
    hierarchy = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['hierarchy']

    def __str__(self):
        return self.name


class DepartmentTeamMembership(models.Model):
    department_team = models.ForeignKey(DepartmentTeam, on_delete=models.CASCADE)
    profile = models.ForeignKey(AdminProfile, on_delete=models.CASCADE)
    hierarchy = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['hierarchy']

    def __str__(self):
        return self.profile.name
