from .views import RegisterView, DisplayProfile, JoinTeam, DisplayTeam
from django.urls import path
from django.conf.urls import url

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    url(r'profile$', DisplayProfile, name='profile'),
    url(r'^myTeam$', DisplayTeam, name='myTeam'),
    url(r'join_team/(?P<teamId>[a-zA-Z0-9]+)$', JoinTeam),
]
