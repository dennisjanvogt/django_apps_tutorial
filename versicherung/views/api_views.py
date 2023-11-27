from django.http import HttpRequest
from ..models import Mitarbeiter, Kunde, Schadensfall, Versicherungsvertrag

from ..serializers import (
    KundeSerializer,
    VersicherungsvertragSerializer,
    SchadensfallSerializer,
    MitarbeiterSerializer,
)
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# MITARBEITER


@api_view(["GET"])
def mitarbeiter_list(request: HttpRequest):
    mitarbeiter = Mitarbeiter.objects.all()
    serializer = MitarbeiterSerializer(mitarbeiter, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def mitarbeiter_create(request: HttpRequest):
    serializer = MitarbeiterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def mitarbeiter_retrieve(request: HttpRequest, pk):
    try:
        mitarbeiter = Mitarbeiter.objects.get(pk=pk)
    except Mitarbeiter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MitarbeiterSerializer(mitarbeiter)
    return Response(serializer.data)


@api_view(["PUT"])
def mitarbeiter_update(request: HttpRequest, pk):
    try:
        mitarbeiter = Mitarbeiter.objects.get(pk=pk)
    except Mitarbeiter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MitarbeiterSerializer(mitarbeiter, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def mitarbeiter_delete(request: HttpRequest, pk):
    try:
        mitarbeiter = Mitarbeiter.objects.get(pk=pk)
    except Mitarbeiter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    mitarbeiter.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# KUNDE


@api_view(["GET"])
def kunde_list(request):
    kunden = Kunde.objects.all()
    serializer = KundeSerializer(kunden, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def kunde_create(request):
    serializer = KundeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def kunde_retrieve(request, pk):
    try:
        kunde = Kunde.objects.get(pk=pk)
    except Kunde.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = KundeSerializer(kunde)
    return Response(serializer.data)


@api_view(["PUT"])
def kunde_update(request, pk):
    try:
        kunde = Kunde.objects.get(pk=pk)
    except Kunde.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = KundeSerializer(kunde, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def kunde_delete(request, pk):
    try:
        kunde = Kunde.objects.get(pk=pk)
    except Kunde.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    kunde.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# VERSICHERUNGSVERTRAG


@api_view(["GET"])
def versvertrag_list(request):
    vertraege = Versicherungsvertrag.objects.all()
    serializer = VersicherungsvertragSerializer(vertraege, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def versvertrag_create(request):
    serializer = VersicherungsvertragSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def versvertrag_retrieve(request, pk):
    try:
        vertrag = Versicherungsvertrag.objects.get(pk=pk)
    except Versicherungsvertrag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = VersicherungsvertragSerializer(vertrag)
    return Response(serializer.data)


@api_view(["PUT"])
def versvertrag_update(request, pk):
    try:
        vertrag = Versicherungsvertrag.objects.get(pk=pk)
    except Versicherungsvertrag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = VersicherungsvertragSerializer(vertrag, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def versvertrag_delete(request, pk):
    try:
        vertrag = Versicherungsvertrag.objects.get(pk=pk)
    except Versicherungsvertrag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    vertrag.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# SCHADEN


@api_view(["GET"])
def schaden_list(request):
    schaeden = Schadensfall.objects.all()
    serializer = SchadensfallSerializer(schaeden, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def schaden_create(request):
    serializer = SchadensfallSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def schaden_retrieve(request, pk):
    try:
        schaden = Schadensfall.objects.get(pk=pk)
    except Schadensfall.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SchadensfallSerializer(schaden)
    return Response(serializer.data)


@api_view(["PUT"])
def schaden_update(request, pk):
    try:
        schaden = Schadensfall.objects.get(pk=pk)
    except Schadensfall.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SchadensfallSerializer(schaden, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def schaden_delete(request, pk):
    try:
        schaden = Schadensfall.objects.get(pk=pk)
    except Schadensfall.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    schaden.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
