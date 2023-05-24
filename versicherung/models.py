from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Mitarbeiter(models.Model):
    class Position(models.TextChoices):
        AGENT = "agent", "Agent"
        MANAGER = "manager", "Manager"
        SUPPORT = "support", "Support"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(
        max_length=100, choices=Position.choices, null=True, blank=True
    )
    geburtsdatum = models.DateField(null=True, blank=True)
    einstellungsdatum = models.DateField(null=True, blank=True)
    telefonnummer = models.CharField(max_length=15, unique=True, null=True, blank=True)

    def __str__(self):
        return self.user.username if self.user else ""


class Kunde(models.Model):
    vorname = models.CharField(max_length=50)
    nachname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefonnummer = models.CharField(max_length=15, unique=True, null=True, blank=True)
    erstellt_am = models.DateTimeField(auto_now_add=True)
    aktualisiert_am = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nachname}, {self.vorname}"


class Versicherungsvertrag(models.Model):
    vertragsnummer = models.CharField(max_length=20, unique=True)
    kunde = models.ForeignKey(Kunde, on_delete=models.CASCADE)
    mitarbeiter = models.ForeignKey(
        Mitarbeiter, on_delete=models.SET_NULL, null=True, blank=True
    )
    startdatum = models.DateField()
    enddatum = models.DateField()
    monatlicher_betrag = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0)]
    )
    abgeschlossen_am = models.DateTimeField(auto_now_add=True)
    aktualisiert_am = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vertragsnummer


class Schadensfall(models.Model):
    class Status(models.TextChoices):
        OFFEN = "offen", "offen"
        BEARBEITET = "bearbeitet", "bearbeitet"
        ABGESCHLOSSEN = "abgeschlossen", "abgeschlossen"

    beschreibung = models.TextField()
    versicherungsvertrag = models.ForeignKey(
        Versicherungsvertrag, on_delete=models.CASCADE
    )
    schadenshoehe = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0)]
    )
    status = models.CharField(max_length=20, choices=Status.choices)
    erstellt_am = models.DateTimeField(auto_now_add=True)
    aktualisiert_am = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.versicherungsvertrag} - {self.beschreibung }"
