from django.views.generic import TemplateView

from mailing.models.mailing import Mailing
from mailing.models.client import Client


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] = Client.objects.all()
        context['mailing'] = Mailing.objects.all()

        return context
