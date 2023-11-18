from django.urls import path
from . import patterns
from ..views.views import home, dashboard

urlpatterns = [
    path("", home, name="home"),
    path("bashboard", dashboard, name="dashboard"),
] + patterns
