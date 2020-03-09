from django import forms
from .models import Match

forms.DateTimeField.input_formats = ['%m/%d/%Y %I:%M %p%z', '%Y-%m-%dT%H:%M']


class MatchForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = ["game", "match_type", "team1", "team2", "venue", "date_time", "max_team_size", "organisers", "about"]

    def clean_team2(self):
        team2 = self.cleaned_data["team2"]
        team1 = self.cleaned_data["team1"]
        if team1 == team2:
            raise forms.ValidationError("BOTH TEAMS CANNOT BE SAME")
        return team2
