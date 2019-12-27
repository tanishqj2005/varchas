from django.views.generic import CreateView
from .models import UserProfile
from .forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/admin'

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
                                                 accomodation_required=kwargs['accomodation_required'],
                                                 city=kwargs['city'],
                                                 no_of_days=kwargs['no_of_days'],
                                                 referral=kwargs['referral']
                                                 )
        userprofile.save()
