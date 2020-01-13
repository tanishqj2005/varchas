from django.views.generic import CreateView
from .forms import CampusAmbassadorForm, TeamRegistrationForm
from django.shortcuts import get_object_or_404
from accounts.models import UserProfile
from django.http import HttpResponse


class CampusAmbassadorRegisterView(CreateView):
    template_name = 'registration/ca_reg.html'
    success_url = '/admin'
    form_class = CampusAmbassadorForm


class TeamFormationView(CreateView):
    form_class = TeamRegistrationForm
    template_name = 'registration/team.html'
    success_url = 'team'

    def form_valid(self, form):
        user = self.request.user
        if user is not None:
            team = form.save()
            team.captian = get_object_or_404(UserProfile, user=user)
            user.teamId = team.teamId
            user.save()
            team.members.add(user)
            team.save()
            # TeamFormationView.create_team(team, **form.cleaned_data)
            return super(TeamFormationView, self).form_valid(form)
        return HttpResponse("404")
