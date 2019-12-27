from django.contrib import admin
from .models import CampusAmbassador


class CampusAmbassadorAdmin(admin.ModelAdmin):
    class Meta:
        model = CampusAmbassador


admin.site.register(CampusAmbassador, CampusAmbassadorAdmin)
