from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from versicherung.forms import VersicherungsvertragForm
from versicherung.models import Versicherungsvertrag


def versicherungsvertrag_list(request: HttpRequest):
    versicherungsvertrag_list = Versicherungsvertrag.objects.all()
    context = {"versicherungsvertrag_list": versicherungsvertrag_list}
    return render(
        request, "versicherungsvertrag/versicherungsvertrag_list.html", context
    )


def versicherungsvertrag_detail(request: HttpRequest, pk: int):
    versicherungsvertrag = get_object_or_404(Versicherungsvertrag, pk=pk)
    context = {"versicherungsvertrag": versicherungsvertrag}
    return render(
        request, "versicherungsvertrag/versicherungsvertrag_detail.html", context
    )


def versicherungsvertrag_create(request: HttpRequest):
    if request.method == "POST":
        form = VersicherungsvertragForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("versicherungsvertrag_list")
    else:
        form = VersicherungsvertragForm()
    return render(
        request, "versicherungsvertrag/versicherungsvertrag_form.html", {"form": form}
    )


def versicherungsvertrag_update(request: HttpRequest, pk: int):
    versicherungsvertrag = get_object_or_404(Versicherungsvertrag, pk=pk)
    if request.method == "POST":
        form = VersicherungsvertragForm(request.POST, instance=versicherungsvertrag)
        if form.is_valid():
            form.save()
            return redirect("versicherungsvertrag_list")
    else:
        form = VersicherungsvertragForm(instance=versicherungsvertrag)
    return render(
        request, "versicherungsvertrag/versicherungsvertrag_form.html", {"form": form}
    )


def versicherungsvertrag_delete(request: HttpRequest, pk: int):
    versicherungsvertrag = get_object_or_404(Versicherungsvertrag, pk=pk)
    if request.method == "POST":
        versicherungsvertrag.delete()
        return redirect("versicherungsvertrag_list")
    return render(
        request,
        "versicherungsvertrag/versicherungsvertrag_confirm_delete.html",
        {"versicherungsvertrag": versicherungsvertrag},
    )
