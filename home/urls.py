from django.urls import path

from home.apps import HomeConfig
from home.views import HomePageView

app_name = HomeConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
]
