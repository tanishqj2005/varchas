from django.urls import path
from .views import IndexView, NavBarSubOptionsPageView

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('<slug:slug>', NavBarSubOptionsPageView.as_view(), name='navbarsuboptionpage'),
]
