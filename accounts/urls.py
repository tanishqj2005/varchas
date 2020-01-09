from .views import RegisterView, DisplayProfile, JoinTeam
from django.urls import path
from django.conf.urls import url


app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    url(r'profile/(?P<username>[a-zA-Z0-9]+)$', DisplayProfile),
    url(r'join_team/(?P<teamId>[a-zA-Z0-9]+)/(?P<username>[a-zA-Z0-9]+)$', JoinTeam),
]
