from django.contrib import admin

from versicherung.models import Mitarbeiter, Kunde, Versicherungsvertrag, Schadensfall

# Register your models here.
admin.site.register(Mitarbeiter)
admin.site.register(Kunde)
admin.site.register(Versicherungsvertrag)
admin.site.register(Schadensfall)
