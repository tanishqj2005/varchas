from .views import CampusAmbassadorRegisterView, TeamFormationView
from django.urls import path
from django.contrib.auth.decorators import login_required
app_name = 'registration'

urlpatterns = [
    path('ca', CampusAmbassadorRegisterView.as_view(), name='ca'),
    path('team', TeamFormationView.as_view(), name='team')
    # url(r'team/(?P<username>[a-zA-Z0-9]+)$',TeamFormationView),

]
