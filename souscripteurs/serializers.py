from rest_framework import serializers
from .models import Souscripteurs, Assureurs


class SouscripteursSerializer(serializers.ModelSerializer):
    # poster = serializers.ReadOnlyField(source='poster.username')
    # poster_id = serializers.ReadOnlyField(source='poster.id')

    class Meta:
        model = Souscripteurs
        fields = ['id', 'nom', 'dateEffet', 'dateEcheance', 'assureur', 'territorialite', 'consultationGeneraliste', 'consultationSpecialiste', 'pharmacie', 'vitamines', 'vaccins', 'hospitalisation', 'created']

class AssureursSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assureurs
        field = ['id', 'nom', 'adresseMail', 'created']