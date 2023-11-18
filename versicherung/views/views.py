from django.http import HttpRequest
from django.db.models import Sum
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Kunde, Mitarbeiter, Versicherungsvertrag, Schadensfall


@login_required(login_url="login")
def home(request: HttpRequest):
    context = {}
    return render(request, "home.html", context)


@login_required(login_url="login")
def dashboard(request):
    kunden_count = Kunde.objects.count()
    mitarbeiter_count = Mitarbeiter.objects.count()
    versicherungsvertrag_count = Versicherungsvertrag.objects.count()
    schadensfall_count = Schadensfall.objects.count()

    total_monatlicher_beitrag = Versicherungsvertrag.objects.aggregate(
        Sum("monatlicher_beitrag")
    )["monatlicher_beitrag__sum"]
    total_schadenshoehe = Schadensfall.objects.aggregate(Sum("schadenshoehe"))[
        "schadenshoehe__sum"
    ]

    if total_monatlicher_beitrag is not None:
        total_monatlicher_beitrag = round(total_monatlicher_beitrag, 2)

    if total_schadenshoehe is not None:
        total_schadenshoehe = round(total_schadenshoehe, 2)

    lukrativste_vertrage = Versicherungsvertrag.objects.order_by(
        "-monatlicher_beitrag"
    )[:3]

    context = {
        "kunden_count": kunden_count,
        "mitarbeiter_count": mitarbeiter_count,
        "versicherungsvertrag_count": versicherungsvertrag_count,
        "schadensfall_count": schadensfall_count,
        "total_monatlicher_beitrag": total_monatlicher_beitrag,
        "total_schadenshoehe": total_schadenshoehe,
        "lukrativste_vertrage": lukrativste_vertrage,
    }

    return render(request, "dashboard.html", context)
