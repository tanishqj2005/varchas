from django.views.generic import CreateView
from .models import UserProfile
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.shortcuts import reverse


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
            return url or self.request.user.userprofile.get_absolute_url()
        elif hasattr(self.request.user, 'adminprofile'):
            return url or reverse('adminportal:index')
        else:
            return reverse('main:home')
