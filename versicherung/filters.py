import django_filters

from versicherung.models import Mitarbeiter


class MitarbeiterFilter(django_filters.FilterSet):
    einstellungsdatum = django_filters.DateFilter(lookup_expr="gte")
    telefonnummer = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Mitarbeiter
        fields = ["position", "einstellungsdatum", "telefonnummer"]
