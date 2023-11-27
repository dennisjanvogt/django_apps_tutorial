from rest_framework import serializers
from .models import Mitarbeiter, Kunde, Versicherungsvertrag, Schadensfall


class MitarbeiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mitarbeiter
        fields = "__all__"


class KundeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kunde
        fields = "__all__"


class VersicherungsvertragSerializer(serializers.ModelSerializer):
    class Meta:
        model = Versicherungsvertrag
        fields = "__all__"


class SchadensfallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schadensfall
        fields = "__all__"
