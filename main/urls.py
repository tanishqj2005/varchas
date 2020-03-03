from django.urls import path
from .views import IndexView, NavBarSubOptionsPageView, OurTeamView, comingSoon, dashboardTeams
from .views import dashboardUsers, dashboard, downloadExcel, dashboardCas, sendMail
from django.conf.urls import url

app_name = 'main'

urlpatterns = [
    url(r'^comingSoon$', comingSoon, name='comingSoon'),
    path('', IndexView.as_view(), name='home'),
    path('admin/mail', sendMail.as_view(), name='mail'),
    url(r'^admin$', dashboard, name='dashboard'),
    url(r'^admin/team$', dashboardTeams, name='dteams'),
    url(r'^admin/users$', dashboardUsers, name='dusers'),
    url(r'^admin/cas$', dashboardCas, name='dcas'),
    url(r'^admin/excel$', downloadExcel, name='teamInfo'),
    path('OurTeam', OurTeamView.as_view(), name='OurTeam'),
    path('<slug:slug>', NavBarSubOptionsPageView.as_view(),
         name='navbarsuboptionpage'),
]
