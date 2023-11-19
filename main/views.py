from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import MitarbeiterRegisterForm


def index(request):
    apps = [
        {
            "name": "Versicherungsorganisation",
            "description": "Implementierung diverser Django Funktionalitäten.",
            "image_url": "/static/images/versicherung.png",
            "url": "/versicherung/",
        },
        # {
        #     "name": "Stopwatch",
        #     "description": "In Arbeit",
        #     "image_url": "/static/images/stopwatch.png",
        #     "url": "/",
        # },
        # {
        #     "name": "Kassenbuch",
        #     "description": "In Arbeit",
        #     "image_url": "/static/images/kassenbuch.png",
        #     "url": "/",
        # },
        # {
        #     "name": "Dokumenten Management System",
        #     "description": "In Arbeit",
        #     "image_url": "/static/images/dms.png",
        #     "url": "/",
        # },
        # {
        #     "name": "Gamification Board",
        #     "description": "Beschreibung None",
        #     "image_url": "/static/images/none.png",
        #     "url": "/",
        # },
        # {
        #     "name": "Datenanalyse",
        #     "description": "Beschreibung None",
        #     "image_url": "/static/images/none.png",
        #     "url": "/",
        # },
        # {
        #     "name": "QuestionsTool",
        #     "description": "Beschreibung None",
        #     "image_url": "/static/images/none.png",
        #     "url": "/",
        # },
    ]

    return render(request, "index.html", {"apps": apps})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        form = MitarbeiterRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = MitarbeiterRegisterForm()
    return render(request, "register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")
