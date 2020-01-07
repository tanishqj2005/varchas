from .views import CampusAmbassadorRegisterView, TeamFormationView
from django.urls import path

app_name = 'registration'

urlpatterns = [
    path('ca', CampusAmbassadorRegisterView.as_view(), name='ca'),
    path('team', TeamFormationView.as_view(), name='team')
]
