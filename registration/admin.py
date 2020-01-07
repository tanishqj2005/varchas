from django.contrib import admin
from .models import CampusAmbassador, TeamRegistration


class CampusAmbassadorAdmin(admin.ModelAdmin):
    class Meta:
        model = CampusAmbassador
admin.site.register(CampusAmbassador, CampusAmbassadorAdmin)

class TeamAdmin(admin.ModelAdmin):
    class Meta:
        model = TeamRegistration

admin.site.register(TeamRegistration,TeamAdmin)
