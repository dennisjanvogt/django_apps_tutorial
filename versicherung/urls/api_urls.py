from django.urls import path

from ..views.api_views import (
    mitarbeiter_list,
    mitarbeiter_create,
    mitarbeiter_retrieve,
    mitarbeiter_update,
    mitarbeiter_delete,
    kunde_list,
    kunde_create,
    kunde_retrieve,
    kunde_update,
    kunde_delete,
    versvertrag_list,
    versvertrag_create,
    versvertrag_retrieve,
    versvertrag_update,
    versvertrag_delete,
    schaden_list,
    schaden_create,
    schaden_retrieve,
    schaden_update,
    schaden_delete,
)


urlpatterns = [
    # MITARBEITER
    path("api/mitarbeiter/", mitarbeiter_list, name="api_mitarbeiter_list"),
    path("api/mitarbeiter/create/", mitarbeiter_create, name="api_mitarbeiter_create"),
    path(
        "api/mitarbeiter/<int:pk>/",
        mitarbeiter_retrieve,
        name="api_mitarbeiter_retrieve",
    ),
    path(
        "api/mitarbeiter/<int:pk>/update/",
        mitarbeiter_update,
        name="api_mitarbeiter_update",
    ),
    path(
        "api/mitarbeiter/<int:pk>/delete/",
        mitarbeiter_delete,
        name="api_mitarbeiter_delete",
    ),
    # KUNDE
    path("api/kunde/", kunde_list, name="api_kunde_list"),
    path("api/kunde/create/", kunde_create, name="api_kunde_create"),
    path("api/kunde/<int:pk>/", kunde_retrieve, name="api_kunde_retrieve"),
    path("api/kunde/<int:pk>/update/", kunde_update, name="api_kunde_update"),
    path("api/kunde/<int:pk>/delete/", kunde_delete, name="api_kunde_delete"),
    # VERSICHERUNGSVERTRAG
    path("api/versvertrag/", versvertrag_list, name="api_versvertrag_list"),
    path("api/versvertrag/create/", versvertrag_create, name="api_ersvertrag_create"),
    path(
        "api/versvertrag/<int:pk>/",
        versvertrag_retrieve,
        name="api_versvertrag_retrieve",
    ),
    path(
        "api/versvertrag/<int:pk>/update/",
        versvertrag_update,
        name="api_versvertrag_update",
    ),
    path(
        "api/versvertrag/<int:pk>/delete/",
        versvertrag_delete,
        name="api_versvertrag_delete",
    ),
    # SCHADEN
    path("api/schaden/", schaden_list, name="api_schaden_list"),
    path("api/schaden/create/", schaden_create, name="api_schaden_create"),
    path("api/schaden/<int:pk>/", schaden_retrieve, name="api_schaden_retrieve"),
    path("api/schaden/<int:pk>/update/", schaden_update, name="api_schaden_update"),
    path("api/schaden/<int:pk>/delete/", schaden_delete, name="api_schaden_delete"),
]
