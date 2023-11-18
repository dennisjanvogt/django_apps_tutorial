from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from versicherung.forms import KundeForm
from versicherung.models import Kunde


def kunde_list(request: HttpRequest):
    kunden = Kunde.objects.all()
    context = {"kunden": kunden}
    return render(request, "kunde/kunde_list.html", context)


def kunde_create(request: HttpRequest):
    if request.method == "POST":
        form = KundeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Kunde wurde erfolgreich erstellt.")
            return redirect("kunde_list")
    else:
        form = KundeForm()
    context = {"form": form}
    return render(request, "kunde/kunde_form.html", context)


def kunde_detail(request: HttpRequest, pk: int):
    kunde = get_object_or_404(Kunde, pk=pk)
    context = {"kunde": kunde}
    return render(request, "kunde/kunde_detail.html", context)


def kunde_update(request: HttpRequest, pk: int):
    kunde = get_object_or_404(Kunde, pk=pk)
    if request.method == "POST":
        form = KundeForm(request.POST, instance=kunde)
        if form.is_valid():
            form.save()
            messages.success(request, "Kunde wurde erfolgreich aktualisiert.")
            return redirect("kunde_list")
    else:
        form = KundeForm(instance=kunde)
    context = {"form": form, "kunde": kunde}
    return render(request, "kunde/kunde_form.html", context)


def kunde_delete(request: HttpRequest, pk: int):
    kunde = get_object_or_404(Kunde, pk=pk)
    if request.method == "POST":
        kunde.delete()
        messages.success(request, "Kunde wurde erfolgreich gelöscht.")
        return redirect("kunde_list")
    context = {"kunde": kunde}
    return render(request, "kunde/kunde_confirm_delete.html", context)
