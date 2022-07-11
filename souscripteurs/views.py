from rest_framework import generics

from .models import Souscripteur, Assureur
from .serializers import SouscripteursSerializer, AssureursSerializer


class SouscripteursList(generics.ListCreateAPIView):
    queryset = Souscripteur.objects.all()
    serializer_class = SouscripteursSerializer


class AssureursList(generics.ListCreateAPIView):
    queryset = Assureur.objects.all()
    serializer_class = AssureursSerializer
