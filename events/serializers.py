from .models import Cricket, Football
from rest_framework import serializers


class CricketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cricket
        fields = ['match', 'run1', 'run2', 'wicket1', 'wicket2', 'overs1', 'overs2']


class FootballSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Football
        fields = ['match', 'score1', 'score2', ]
