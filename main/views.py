from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
# from .utils import SiteAccessMixin
from django.contrib.auth.decorators import login_required
from .models import HomeImageCarousel, NavBarSubOptions, HomeEventCard, HomeBriefCard, OurTeam
from django.shortcuts import get_object_or_404, render
from accounts.models import UserProfile
from registration.models import TeamRegistration, CampusAmbassador
import csv
from django.http import HttpResponse


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        if self.request.user.username != "":
            userprofile = get_object_or_404(
                UserProfile, user=self.request.user)
        context = super(IndexView, self).get_context_data(**kwargs)
        context['carousel'] = HomeImageCarousel.objects.filter(
            active=True).order_by('ordering')
        context['event_list'] = HomeEventCard.objects.all
        context['brief_list'] = HomeBriefCard.objects.all
        if self.request.user.username != "":
            context['userprofile'] = userprofile
        return context


class NavBarSubOptionsPageView(DetailView):
    template_name = 'main/navbarsuboptionpage.html'
    model = NavBarSubOptions

    def get_context_data(self, **kwargs):
        context = super(NavBarSubOptionsPageView, self).get_context_data()
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if self.object.use_custom_html:
            self.template_name = self.object.custom_html
        else:
            self.template_name = 'main/navbarsuboptionpage.html'
        return self.render_to_response(context)


class OurTeamView(TemplateView):
    template_name = 'main/our_team.html'
    model = OurTeam

    def get_context_data(self, **kwargs):
        context = super(OurTeamView, self).get_context_data(**kwargs)
        context["our_team"] = OurTeam.objects.all
        return context


@login_required(login_url='login')
def dashboard(request):
    if not request.user.is_superuser:
        return render(request, "404")
    teams = TeamRegistration.objects.all()
    nteams = teams.count()
    users = UserProfile.objects.all()
    nusers = users.count()
    cas = CampusAmbassador.objects.all()
    ncas = cas.count()
    return render(request, 'main/dashboard.html', {'user': request.user, 'nteams': nteams, 'nusers': nusers, 'ncas': ncas})


@login_required(login_url='login')
def dashboardTeams(request):
    teams = TeamRegistration.objects.all()
    return render(request, 'main/dashboardTeams.html', {'teams': teams})


@login_required(login_url='login')
def dashboardUsers(request):
    users = UserProfile.objects.all()
    return render(request, 'main/dashboardUsers.html', {'users': users})


@login_required(login_url='login')
def dashboardCas(request):
    cas = CampusAmbassador.objects.all()
    return render(request, 'main/dashboardCas.html', {'cas': cas})


@login_required(login_url='login')
def downloadExcel(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="teams.csv"'
    writer = csv.writer(response)
    writer.writerow(['TeamID', 'Sport', 'Captian', 'College', 'Members'])
    teams = TeamRegistration.objects.all()
    for team in teams:
        members = []
        for member in team.members.all():
            members.append(member.user.first_name)
        writer.writerow([team, team.get_sport_display(), team.captian.user.first_name, team.college, ", ".join(members)])
    return response


def comingSoon(request):
    return render(request, 'main/comingSoon.html')


def error_404(request, exception):
    return render(request, 'main/error_404.html', status=404)


def error_500(request):
    return render(request, 'main/error_500.html', status=500)
