from django.urls import path

from ..views.schadensfall_views import (
    schadensfall_create,
    schadensfall_delete,
    schadensfall_detail,
    schadensfall_list,
    schadensfall_update,
)

urlpatterns = [
    path("schadensfall/", schadensfall_list, name="schadensfall_list"),
    path("schadensfall/<int:pk>/", schadensfall_detail, name="schadensfall_detail"),
    path("schadensfall/neu/", schadensfall_create, name="schadensfall_create"),
    path(
        "schadensfall/<int:pk>/bearbeiten/",
        schadensfall_update,
        name="schadensfall_update",
    ),
    path(
        "schadensfall/<int:pk>/loeschen/",
        schadensfall_delete,
        name="schadensfall_delete",
    ),
]
