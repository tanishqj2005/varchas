from django import forms
from .models import Match


# forms.TimeField.input_formats = ['%I:%M %p%z'] #['%Y-%m-%dT%H:%M']

class MatchForm(forms.ModelForm):
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

    class Meta:
        model = Match
        fields = ["event", "match_type", "team1", "team2", "venue", "time",
                  "date_time", "max_team_size", "organisers", "about"]

    def clean_team2(self):
        team2 = self.cleaned_data["team2"]
        team1 = self.cleaned_data["team1"]
        if team1 == team2:
            raise forms.ValidationError("BOTH TEAMS CANNOT BE SAME")
        return team2
