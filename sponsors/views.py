from django.views.generic import ListView
from .models import SponsorType, Sponsor
from rest_framework import viewsets
from .serializers import SponsorSerializer


class SponsorView(ListView):
    model = SponsorType
    template_name = 'sponsors/index.html'


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
