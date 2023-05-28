# Generated by Django 4.1.7 on 2023-05-24 17:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Kunde",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vorname", models.CharField(max_length=50)),
                ("nachname", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "telefonnummer",
                    models.CharField(blank=True, max_length=15, null=True, unique=True),
                ),
                ("erstellt_am", models.DateTimeField(auto_now_add=True)),
                ("aktualisiert_am", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Mitarbeiter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "position",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("agent", "Agent"),
                            ("manager", "Manager"),
                            ("support", "Support"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                ("geburtsdatum", models.DateField(blank=True, null=True)),
                ("einstellungsdatum", models.DateField(blank=True, null=True)),
                (
                    "telefonnummer",
                    models.CharField(blank=True, max_length=15, null=True, unique=True),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Versicherungsvertrag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vertragsnummer", models.CharField(max_length=20, unique=True)),
                ("startdatum", models.DateField()),
                ("enddatum", models.DateField()),
                (
                    "monatlicher_betrag",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=8,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("abgeschlossen_am", models.DateTimeField(auto_now_add=True)),
                ("aktualisiert_am", models.DateTimeField(auto_now=True)),
                (
                    "kunde",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="versicherung.kunde",
                    ),
                ),
                (
                    "mitarbeiter",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="versicherung.mitarbeiter",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Schadensfall",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("beschreibung", models.TextField()),
                (
                    "schadenshoehe",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=8,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("offen", "offen"),
                            ("bearbeitet", "bearbeitet"),
                            ("abgeschlossen", "abgeschlossen"),
                        ],
                        max_length=20,
                    ),
                ),
                ("erstellt_am", models.DateTimeField(auto_now_add=True)),
                ("aktualisiert_am", models.DateTimeField(auto_now=True)),
                (
                    "versicherungsvertrag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="versicherung.versicherungsvertrag",
                    ),
                ),
            ],
        ),
    ]