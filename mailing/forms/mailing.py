from django import forms

from mailing.models.mailing import Mailing


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ['title', 'body', 'mailing_time', 'frequency', 'status', 'clients',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

