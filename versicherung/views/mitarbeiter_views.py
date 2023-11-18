import csv
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from versicherung.forms import MitarbeiterForm
from versicherung.models import Mitarbeiter
from versicherung.filters import MitarbeiterFilter

from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def mitarbeiter_list(request: HttpRequest):
    mitarbeiter_filter = MitarbeiterFilter(
        request.GET, queryset=Mitarbeiter.objects.all()
    )
    context = {"filter": mitarbeiter_filter}
    return render(request, "mitarbeiter/mitarbeiter_list.html", context)


@login_required(login_url="login")
def mitarbeiter_create(request: HttpRequest):
    if request.method == "POST":
        form = MitarbeiterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Mitarbeiter wurde erfolgreich erstellt.")
            return redirect("mitarbeiter_list")
    else:
        form = MitarbeiterForm()
    context = {"form": form}
    return render(request, "mitarbeiter/mitarbeiter_form.html", context)


@login_required(login_url="login")
def mitarbeiter_detail(request: HttpRequest, pk: int):
    mitarbeiter = get_object_or_404(Mitarbeiter, pk=pk)
    context = {"mitarbeiter": mitarbeiter}
    return render(request, "mitarbeiter/mitarbeiter_detail.html", context)


@login_required(login_url="login")
def mitarbeiter_update(request: HttpRequest, pk: int):
    mitarbeiter = get_object_or_404(Mitarbeiter, pk=pk)
    if request.method == "POST":
        form = MitarbeiterForm(request.POST, instance=mitarbeiter)
        if form.is_valid():
            form.save()
            messages.success(request, "Mitarbeiter wurde erfolgreich aktualisiert.")
            return redirect("mitarbeiter_list")
    else:
        form = MitarbeiterForm(instance=mitarbeiter)
    context = {"form": form, "mitarbeiter": mitarbeiter}
    return render(request, "mitarbeiter/mitarbeiter_form.html", context)


@login_required(login_url="login")
def mitarbeiter_delete(request: HttpRequest, pk: int):
    mitarbeiter = get_object_or_404(Mitarbeiter, pk=pk)
    if request.method == "POST":
        mitarbeiter.delete()
        messages.success(request, "Mitarbeiter wurde erfolgreich gelöscht.")
        return redirect("mitarbeiter_list")
    context = {"mitarbeiter": mitarbeiter}
    return render(request, "mitarbeiter/mitarbeiter_confirm_delete.html", context)


def export_mitarbeiter_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="mitarbeiter.csv"'

    writer = csv.writer(response)
    writer.writerow(["ID", "Name", "Position", "Einstellungsdatum", "Telefonnummer"])

    mitarbeiter_filter = MitarbeiterFilter(
        request.GET, queryset=Mitarbeiter.objects.all()
    )
    for mitarbeiter in mitarbeiter_filter.qs.values_list(
        "id", "user", "position", "einstellungsdatum", "telefonnummer"
    ):
        writer.writerow(mitarbeiter)

    return response
