from django.urls import path
from .views import IndexView, NavBarSubOptionsPageView, OurTeamView

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('OurTeam', OurTeamView.as_view(), name='OurTeam'),
    path('<slug:slug>', NavBarSubOptionsPageView.as_view(),
         name='navbarsuboptionpage'),
]
