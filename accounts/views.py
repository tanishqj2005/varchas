from django.views.generic import CreateView
from .models import UserProfile
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.shortcuts import reverse, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from registration.models import TeamRegistration
from django.http import HttpResponse


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        data = self.request.POST.copy()
        data['username'] = data['email']
        form = RegisterForm(data)
        user = form.save()
        RegisterView.create_profile(user, **form.cleaned_data)
        # messages.success(self.request, 'Hi %s,' % user.get_full_name())
        return super(RegisterView, self).form_valid(form)

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    @staticmethod
    def create_profile(user=None, **kwargs):
        userprofile = UserProfile.objects.create(user=user, gender=kwargs['gender'], phone=kwargs['phone'],
                                                 college=kwargs['college'],
                                                 state=kwargs['state'],
                                                 accommodation_required=kwargs['accommodation_required'],
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


@login_required(login_url="login")
def DisplayProfile(request):
    user = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'accounts/profile.html', {'userprofile': user, 'user': request.user, 'page': "profile"})


@login_required(login_url="login")
def DisplayTeam(request):
    user = get_object_or_404(UserProfile, user=request.user)
    teamId = user.teamId
    team = get_object_or_404(TeamRegistration, teamId=teamId)
    return render(request, 'accounts/myTeam.html', {'profile_team': team, 'profile_user': user, 'page': "team"})


@login_required(login_url="login")
def leaveTeam(request):
    user = get_object_or_404(UserProfile, user=request.user)
    teamId = user.teamId
    user.teamId = "NULL"
    user.save()
    team = get_object_or_404(TeamRegistration, teamId=teamId)
    team.members.remove(user)
    return redirect('main:home')


@login_required(login_url="login")
def joinTeam(request):
    user = request.user
    if request.method == 'POST':
        teamId = request.POST.get('teamId')
        if user is not None:
            user = get_object_or_404(UserProfile, user=user)
            if user.teamId != "NULL":
                message = "You are already in team {}".format(user.teamId)
                message += "\nYou have to register again to join another team. \nContact Varchas administrators."
                return HttpResponse(message, content_type="text/plain")
            team = get_object_or_404(TeamRegistration, teamId=teamId)
            user.teamId = teamId
            user.save()
            team.members.add(user)
            return redirect('accounts:myTeam')
        return reverse('login')
    return render(request, 'accounts/joinTeam.html')
