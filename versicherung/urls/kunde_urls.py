from django.urls import path

from ..views.kunde_views import (
    kunde_create,
    kunde_delete,
    kunde_detail,
    kunde_list,
    kunde_update,
)

urlpatterns = [
    path("kunden/", kunde_list, name="kunde_list"),
    path("kunden/neu/", kunde_create, name="kunde_create"),
    path("kunden/<int:pk>/", kunde_detail, name="kunde_detail"),
    path("kunden/<int:pk>/bearbeiten/", kunde_update, name="kunde_update"),
    path("kunden/<int:pk>/loeschen/", kunde_delete, name="kunde_delete"),
]
