from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from versicherung.forms import SchadensfallForm
from versicherung.models import Schadensfall


def schadensfall_list(request: HttpRequest):
    schadensfall_list = Schadensfall.objects.all()
    context = {"schadensfall_list": schadensfall_list}
    return render(request, "schadensfall/schadensfall_list.html", context)


def schadensfall_detail(request: HttpRequest, pk: int):
    schadensfall = get_object_or_404(Schadensfall, pk=pk)
    context = {"schadensfall": schadensfall}
    return render(request, "schadensfall/schadensfall_detail.html", context)


def schadensfall_create(request: HttpRequest):
    if request.method == "POST":
        form = SchadensfallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("schadensfall_list")
    else:
        form = SchadensfallForm()
    return render(request, "schadensfall/schadensfall_form.html", {"form": form})


def schadensfall_update(request: HttpRequest, pk: int):
    schadensfall = get_object_or_404(Schadensfall, pk=pk)
    if request.method == "POST":
        form = SchadensfallForm(request.POST, instance=schadensfall)
        if form.is_valid():
            form.save()
            return redirect("schadensfall_list")
    else:
        form = SchadensfallForm(instance=schadensfall)
    return render(request, "schadensfall/schadensfall_form.html", {"form": form})


def schadensfall_delete(request: HttpRequest, pk: int):
    schadensfall = get_object_or_404(Schadensfall, pk=pk)
    if request.method == "POST":
        schadensfall.delete()
        return redirect("schadensfall_list")
    return render(
        request,
        "schadensfall/schadensfall_confirm_delete.html",
        {"schadensfall": schadensfall},
    )
