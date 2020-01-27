from django.views.generic import CreateView
from .forms import CampusAmbassadorForm, TeamRegistrationForm, TeamRegistrationForm1
from django.shortcuts import get_object_or_404
from accounts.models import UserProfile
from django.http import HttpResponse
from random import random
from .models import TeamRegistration
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials


class CampusAmbassadorRegisterView(CreateView):
    template_name = 'registration/ca_reg.html'
    success_url = '/admin'
    form_class = CampusAmbassadorForm


class TeamFormationView(CreateView):
    form_class = TeamRegistrationForm
    template_name = 'registration/team.html'
    success_url = '/account/myTeam'

    def form_valid(self, form):
        user = self.request.user
        if user is not None:
            data = self.request.POST.copy()
            spor = TeamRegistration.SPORT_CHOICES[int(data['sport'])-1][1][:3]
            data['teamId'] = "VA-" + spor[:3].upper() + '-' + user.username[:3].upper() + "{}".format(int(random()*100))
            form = TeamRegistrationForm1(data)
            user = get_object_or_404(UserProfile, user=user)
            if user.teamId != "NULL":
                message = "You are already in team {}".format(user.teamId)
                message += "\nYou have to register again to join another team. \nContact Varchas administrators."
                return HttpResponse(message, content_type="text/plain")
            team = form.save()
            team.captian = user
            user.teamId = team.teamId
            user.save()
            team.members.add(user)

            # Adding Data to google sheet

            # scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
            # creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
            # client = gspread.authorize(creds)
            # sheet = client.open('Varchas-Teams').sheet1
            # row = [team.teamId, team.get_sport_display(), team.captian.user.first_name, team.captian.phone,team.college]
            # sheet.insert_row(row, 2) # inserting row at the top

            # team.save()
            return super(TeamFormationView, self).form_valid(form)
        return HttpResponse("404")
