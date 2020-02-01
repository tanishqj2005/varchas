from django.urls import path
from .views import IndexView, NavBarSubOptionsPageView, OurTeamView, comingSoon, dashboardTeams
from .views import dashboardUsers, dashboard, downloadExcel
from django.conf.urls import url

app_name = 'main'

urlpatterns = [
    url(r'^comingSoon$', comingSoon, name='comingSoon'),
    path('', IndexView.as_view(), name='home'),
    url(r'^admin/dashboard$', dashboard, name='dashboard'),
    url(r'^admin/dashboard/team$', dashboardTeams, name='dteams'),
    url(r'^admin/dashboard/users$', dashboardUsers, name='dusers'),
    url(r'^admin/dashboard/excel$', downloadExcel, name='teamInfo'),
    path('OurTeam', OurTeamView.as_view(), name='OurTeam'),
    path('<slug:slug>', NavBarSubOptionsPageView.as_view(),
         name='navbarsuboptionpage'),
]
