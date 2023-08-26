from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from mailing.forms.client import ClientForm
from mailing.forms.mailing import MailingForm
from mailing.models.client import Client
from mailing.models.mailing import Mailing


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = 'home:index'


class MailingListView(ListView):
    model = Mailing

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        return queryset


class MailingDetailView(DetailView):
    model = Mailing


class MailingDeleteView(DeleteView):
    model = Mailing


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = 'mailing:mailing_list'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = 'home:index'
