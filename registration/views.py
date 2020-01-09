from django.views.generic import CreateView
from .forms import CampusAmbassadorForm, TeamRegistrationForm
#from django.utils.decorators import method_decorator


class CampusAmbassadorRegisterView(CreateView):
    template_name = 'registration/ca_reg.html'
    success_url = '/admin'
    form_class = CampusAmbassadorForm

#@method_decorator(login_required, name='dispatch')
class TeamFormationView(CreateView):
    template_name = 'registration/team.html'
    success_url = 'team'
    form_class = TeamRegistrationForm

# @login_required
# def TeamFormationView(request, username):
#     user = get_object_or_404(User, username=username)
#     user = get_object_or_404(UserProfile, user=user)
#     return HttpResponse
