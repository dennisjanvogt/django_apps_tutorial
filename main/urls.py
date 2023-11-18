from django.urls import path
from .views import index, login_view, logout_view, register_view


urlpatterns = [
    path("", index, name="index"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
]
