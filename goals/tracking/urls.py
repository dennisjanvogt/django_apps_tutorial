from django.contrib import admin
from django.urls import path, include

from .views import all_goals

urlpatterns = [
    path('', view=all_goals, name="all_goals")
]