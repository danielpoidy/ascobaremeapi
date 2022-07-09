from rest_framework import generics

from .models import Souscripteurs, Assureurs
from .serializers import SouscripteursSerializer, AssureursSerializer


class SouscripteursList(generics.ListCreateAPIView):
    queryset = Souscripteurs.objects.all()
    serializer_class = SouscripteursSerializer


class AssureursList(generics.ListCreateAPIView):
    queryset = Assureurs.objects.all()
    serializer_class = AssureursSerializer
