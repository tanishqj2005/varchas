from django.contrib import admin
from .models import Sport, Event, Cricket, Volleyball, Football


class SportAdmin(admin.ModelAdmin):
    class Meta:
        model = Sport


admin.site.register(Sport, SportAdmin)


class EventAdmin(admin.ModelAdmin):
    class Meta:
        model = Event


admin.site.register(Event, EventAdmin)


class CricketAdmin(admin.ModelAdmin):
    class Meta:
        model = Cricket


admin.site.register(Cricket, CricketAdmin)


class FootballAdmin(admin.ModelAdmin):
    class Meta:
        model = Football


admin.site.register(Football, FootballAdmin)


class VolleyballAdmin(admin.ModelAdmin):
    class Meta:
        model = Volleyball


admin.site.register(Volleyball, VolleyballAdmin)
