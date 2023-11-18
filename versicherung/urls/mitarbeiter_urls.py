from django.urls import path

from ..views.mitarbeiter_views import (
    export_mitarbeiter_csv,
    mitarbeiter_list,
    mitarbeiter_create,
    mitarbeiter_delete,
    mitarbeiter_detail,
    mitarbeiter_update,
)

urlpatterns = [
    path("mitarbeiter/", mitarbeiter_list, name="mitarbeiter_list"),
    path("mitarbeiter/create/", mitarbeiter_create, name="mitarbeiter_create"),
    path("mitarbeiter/<int:pk>/", mitarbeiter_detail, name="mitarbeiter_detail"),
    path(
        "mitarbeiter/<int:pk>/update/",
        mitarbeiter_update,
        name="mitarbeiter_update",
    ),
    path(
        "mitarbeiter/<int:pk>/delete/",
        mitarbeiter_delete,
        name="mitarbeiter_delete",
    ),
    path(
        "mitarbeiter/export_csv/", export_mitarbeiter_csv, name="export_mitarbeiter_csv"
    ),
]
