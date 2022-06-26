from django.contrib import admin
from .models import Assureurs, Souscripteurs


class AssureursAdmin(admin.ModelAdmin):
    list_display = ("nom", "adresseMail", "created")


class SouscripteursAdmin(admin.ModelAdmin):
    list_display = ("nom", "dateEffet", "dateEcheance", "assureur")


admin.site.register(Assureurs, AssureursAdmin)
admin.site.register(Souscripteurs, SouscripteursAdmin)

