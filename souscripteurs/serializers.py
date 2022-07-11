from rest_framework import serializers
from .models import Souscripteur, Assureur


class SouscripteursSerializer(serializers.ModelSerializer):
    # poster = serializers.ReadOnlyField(source='poster.username')
    # poster_id = serializers.ReadOnlyField(source='poster.id')

    class Meta:
        model = Souscripteur
        fields = ['id', 'nom', 'dateEffet', 'dateEcheance', 'assureur', 'territorialite', 'consultationGeneraliste', 'consultationSpecialiste', 'pharmacie', 'vitamines', 'vaccins', 'hospitalisation', 'created']


class AssureursSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assureur
        field = ['id', 'nom', 'adresseMail', 'created']