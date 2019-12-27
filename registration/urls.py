from .views import CampusAmbassadorRegisterView
from django.urls import path

app_name = 'registration'

urlpatterns = [
    path('ca', CampusAmbassadorRegisterView.as_view(), name='ca'),
]
