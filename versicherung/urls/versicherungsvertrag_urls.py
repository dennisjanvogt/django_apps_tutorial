from django.urls import path

from ..views.versicherungsvertrag_views import (
    versicherungsvertrag_create,
    versicherungsvertrag_delete,
    versicherungsvertrag_detail,
    versicherungsvertrag_list,
    versicherungsvertrag_update,
)

urlpatterns = [
    path(
        "versicherungsvertrag/",
        versicherungsvertrag_list,
        name="versicherungsvertrag_list",
    ),
    path(
        "versicherungsvertrag/<int:pk>/",
        versicherungsvertrag_detail,
        name="versicherungsvertrag_detail",
    ),
    path(
        "versicherungsvertrag/neu/",
        versicherungsvertrag_create,
        name="versicherungsvertrag_create",
    ),
    path(
        "versicherungsvertrag/<int:pk>/bearbeiten/",
        versicherungsvertrag_update,
        name="versicherungsvertrag_update",
    ),
    path(
        "versicherungsvertrag/<int:pk>/loeschen/",
        versicherungsvertrag_delete,
        name="versicherungsvertrag_delete",
    ),
]
