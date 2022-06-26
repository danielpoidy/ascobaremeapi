from rest_framework import generics

from .models import Souscripteurs
from .serializers import SouscripteursSerializer


class SouscripteursList(generics.ListCreateAPIView):
    queryset = Souscripteurs.objects.all()
    serializer_class = SouscripteursSerializer
