from django import forms
from .models import Kunde, Mitarbeiter, Schadensfall, Versicherungsvertrag


class MitarbeiterForm(forms.ModelForm):
    class Meta:
        model = Mitarbeiter
        fields = "__all__"
        widgets = {
            "geburtsdatum": forms.DateInput(attrs={"type": "date"}),
            "einstellungsdatum": forms.DateInput(attrs={"type": "date"}),
        }


class SchadensfallForm(forms.ModelForm):
    versicherungsvertrag = forms.ModelChoiceField(
        queryset=Versicherungsvertrag.objects.all(), empty_label="(Keine Auswahl)"
    )

    class Meta:
        model = Schadensfall
        fields = "__all__"


class VersicherungsvertragForm(forms.ModelForm):
    kunde = forms.ModelChoiceField(
        queryset=Kunde.objects.all(), empty_label="(Keine Auswahl)"
    )
    mitarbeiter = forms.ModelChoiceField(
        queryset=Mitarbeiter.objects.all(), empty_label="(Keine Auswahl)"
    )

    class Meta:
        model = Versicherungsvertrag
        fields = "__all__"
        widgets = {
            "startdatum": forms.DateInput(attrs={"type": "date"}),
            "enddatum": forms.DateInput(attrs={"type": "date"}),
        }


class KundeForm(forms.ModelForm):
    class Meta:
        model = Kunde
        fields = "__all__"
