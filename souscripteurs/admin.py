from django.contrib import admin
from .models import Assureur, Souscripteur


class AssureursAdmin(admin.ModelAdmin):
    list_display = ("nom", "adresseMail", "created")


class SouscripteursAdmin(admin.ModelAdmin):
    list_display = ("nom", "dateEffet", "dateEcheance", "assureur")


admin.site.register(Assureur, AssureursAdmin)
admin.site.register(Souscripteur, SouscripteursAdmin)

