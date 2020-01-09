from django.views.generic import CreateView
from .models import UserProfile
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from registration.models import TeamRegistration
from django.http import HttpResponse


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        user = form.save()
        RegisterView.create_profile(user, **form.cleaned_data)
        # messages.success(self.request, 'Hi %s,' % user.get_full_name())
        return super(RegisterView, self).form_valid(form)

    @staticmethod
    def create_profile(user=None, **kwargs):
        # Creates a new UserProfile object after successful creation of User object
        userprofile = UserProfile.objects.create(user=user, gender=kwargs['gender'], phone=kwargs['phone'],
                                                 college=kwargs['college'], address=kwargs['address'],
                                                 state=kwargs['state'],
                                                 accomodation_required=kwargs['accommodation_required'],
                                                 # no_of_days=kwargs['no_of_days'],
                                                 referral=kwargs['referred_by']
                                                 )
        userprofile.save()


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_redirect_url(self):
        url = super(CustomLoginView, self).get_redirect_url()
        if hasattr(self.request.user, 'userprofile'):
            return reverse('main:home')
            # return url or self.request.UserProfile.get_absolute_url()
        elif hasattr(self.request.user, 'adminprofile'):
            return url or reverse('adminportal:index')
        else:
            return reverse('main:home')


@login_required
def DisplayProfile(request, username):
    user = get_object_or_404(User, username=username)
    user = get_object_or_404(UserProfile, user=user)
    return render(request, 'accounts/profile.html', {'profile_user': user})


@login_required
def JoinTeam(request, teamId, username):
    team = get_object_or_404(TeamRegistration, teamId=teamId)
    user = get_object_or_404(User, username=username)
    user = get_object_or_404(UserProfile, user=user)
    user.teamId = teamId
    user.save()
    team.members.add(user)
    return HttpResponse("Player {} added to team {}".format(username, teamId))
