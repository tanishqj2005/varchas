from django.views.generic import CreateView
from .forms import CampusAmbassadorForm, TeamRegistrationForm


class CampusAmbassadorRegisterView(CreateView):
    template_name = 'registration/ca_reg.html'
    success_url = '/admin'
    form_class = CampusAmbassadorForm


class TeamFormationView(CreateView):
    template_name = 'registration/team.html'
    success_url = 'team'
    form_class = TeamRegistrationForm
    # def __init__(self):
    #     print(self.username)
