from django.views.generic import ListView
from .models import SponsorType


class SponsorView(ListView):
    model = SponsorType
    template_name = 'sponsors/index.html'
