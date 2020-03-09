from django.views.generic import FormView
from .forms import MatchForm
from .models import Match
from django.contrib import messages


class CreateMatch(FormView):
    template_name = 'events/add_match.html'
    form_class = MatchForm
    success_url = '/events/add'

    def form_valid(self, form):
        data = self.request.POST.copy()
        game_ch = Match.GAME_CHOICES[int(data['game'])-1][1][:2].upper()
        type_ch = Match.MATCH_CHOICES[int(data['match_type'])-1][1][:2].upper()
        data['event_id'] = game_ch + '-' + type_ch + '-' + data['team1'][:2].upper() + data['team2'][:2].upper()
        form = MatchForm(data)
        if Match.objects.filter(event_id=data['event_id']).exists():
            message = "You are already in team {}".format(data['event_id'])
        else:
            message = "Match created with Match ID {}".format(data['event_id'])
            obj = form.save()
            obj.event_id = data['event_id']
            obj.save()
        messages.success(self.request, message)
        # return HttpResponse(message, content_type="text/plain")
        return super(CreateMatch, self).form_valid(form)

    def get_template_names(self):
        if not self.request.user.is_superuser:
            return "main/error_404.html"
        return super().get_template_names()
