from .views import CreateMatch, CricketViewSet
from django.urls import path, include
from rest_framework import routers

app_name = 'events'

router = routers.DefaultRouter()
router.register(r'cricket', CricketViewSet)

urlpatterns = [
    path('add', CreateMatch.as_view(), name='add_match'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
