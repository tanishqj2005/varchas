from django.urls import path
from .views import IndexView, NavBarSubOptionsPageView, OurTeamView, comingSoon, AdminView, downloadPDF
from django.conf.urls import url

app_name = 'main'

urlpatterns = [
    url(r'^comingSoon$', comingSoon, name='comingSoon'),
    path('', IndexView.as_view(), name='home'),
    url(r'^admin/dashboard$', AdminView, name='dashboard'),
    url(r'^admin/dashboard/pdf$', downloadPDF, name='teamInfo'),
    path('OurTeam', OurTeamView.as_view(), name='OurTeam'),
    path('<slug:slug>', NavBarSubOptionsPageView.as_view(),
         name='navbarsuboptionpage'),

]
