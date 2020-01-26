from django.urls import path
from .views import IndexView, NavBarSubOptionsPageView, OurTeamView, comingSoon, AdminView
from django.conf.urls import url

app_name = 'main'

urlpatterns = [
    url(r'^comingSoon$', comingSoon, name='comingSoon'),
    path('', IndexView.as_view(), name='home'),
    url(r'^admin/dashboard$', AdminView, name='dashboard'),
    path('OurTeam', OurTeamView.as_view(), name='OurTeam'),
    path('<slug:slug>', NavBarSubOptionsPageView.as_view(),
         name='navbarsuboptionpage'),

]
