from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingCreateView, MailingListView, ClientCreateView

app_name = MailingConfig.name


urlpatterns = [
    path('create', MailingCreateView.as_view(), name='mailing_create'),
    path('', MailingListView.as_view(), name='mailing_list'),
    path('client_create', ClientCreateView.as_view(), name='client_create'),
]