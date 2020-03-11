from .views import CreateSport
from django.urls import path

app_name = 'events'

urlpatterns = [
    path('add', CreateSport.as_view(), name='add_match')
]
