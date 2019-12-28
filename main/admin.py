from django.contrib import admin
from .models import HomeImageCarousel

class HomeImageCarouselAdmin(admin.ModelAdmin):
    class Meta:
        model = HomeImageCarousel

admin.site.register(HomeImageCarousel ,HomeImageCarouselAdmin)