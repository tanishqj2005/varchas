from django.views.generic import CreateView
from .forms import CampusAmbassadorForm, TeamRegistrationForm


class CampusAmbassadorRegisterView(CreateView):
    template_name = 'registration/ca_reg.html'
    success_url = '/admin'
    form_class = CampusAmbassadorForm


class TeamFormationView(CreateView):
    template_name = 'registration/team.html'
    success_url = ''
    form_class = TeamRegistrationForm
