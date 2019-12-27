from django.urls import path
from .views import SponsorView

app_name = 'sponsor'

urlpatterns = [
    path('', SponsorView.as_view(), name='index'),
]
