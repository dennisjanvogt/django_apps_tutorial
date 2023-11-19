from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from versicherung.models import Mitarbeiter


class MitarbeiterRegisterForm(UserCreationForm):
    position = forms.ChoiceField(choices=Mitarbeiter.Position.choices)
    geburtsdatum = forms.DateField()
    einstellungsdatum = forms.DateField()
    telefonnummer = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "position",
            "geburtsdatum",
            "einstellungsdatum",
            "telefonnummer",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)

        user.save(commit=True)

        mitarbeiter = Mitarbeiter(
            user=user,
            position=self.cleaned_data["position"],
            geburtsdatum=self.cleaned_data["geburtsdatum"],
            einstellungsdatum=self.cleaned_data["einstellungsdatum"],
            telefonnummer=self.cleaned_data["telefonnummer"],
        )
        if commit:
            mitarbeiter.save()

        return user
