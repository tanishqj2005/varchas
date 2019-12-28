from django.views.generic import TemplateView
# from .utils import SiteAccessMixin
from .models import HomeImageCarousel


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['carousel'] = HomeImageCarousel.objects.filter(active=True).order_by('ordering')
        return context
