from django.views.generic import CreateView
from .forms import CampusAmbassadorForm


class CampusAmbassadorRegisterView(CreateView):
    template_name = 'registration/ca_reg.html'
    success_url = '/admin'
    form_class = CampusAmbassadorForm
