from .views import CreateMatch
from django.urls import path

app_name = 'events'

urlpatterns = [
    path('add', CreateMatch.as_view(), name='add_match')
]
