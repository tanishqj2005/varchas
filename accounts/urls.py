from .views import RegisterView, DisplayProfile, joinTeam, DisplayTeam, leaveTeam
from django.urls import path
from django.conf.urls import url

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    url(r'profile$', DisplayProfile, name='profile'),
    url(r'^myTeam$', DisplayTeam, name='myTeam'),
    url(r'joinTeam$', joinTeam, name='joinTeam'),
    url(r'^leaveTeam$', leaveTeam, name='leaveTeam'),

]
