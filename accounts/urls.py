from .views import RegisterView, DisplayProfile, JoinTeam, DisplayTeam
from django.urls import path
from django.conf.urls import url

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    url(r'profile/(?P<username>[a-zA-Z0-9]+)$', DisplayProfile),
    url(r'Myteam', DisplayTeam, name='Myteam'),
    url(r'join_team/(?P<teamId>[a-zA-Z0-9]+)$', JoinTeam),
]
