from datetime import datetime

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from mailing.forms.client import ClientForm
from mailing.forms.mailing import MailingForm
from mailing.models.client import Client
from mailing.models.mailing import Mailing
from mailing.services import send_email


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        #
        # mailing = form.save()
        # clients = mailing.clients.all()
        # # if mailing.mailing_time <= timezone.make_aware(datetime.now(), timezone.get_current_timezone()):
        # #     mailing.status = mailing.Status.COMPLETED
        # #     mailing.save()
        # for client in clients:
        #     send_email(mailing, client)
        return response


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('home:index')


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = 'mailing:mailing_list'


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('home:index')


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('home:index')
