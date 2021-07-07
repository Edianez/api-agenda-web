from rest_framework import generics
from compromisso.api import serializers
from compromisso import models


class CompromissoList(generics.ListCreateAPIView):
    queryset = models.Compromisso.objects.all()
    serializer_class = serializers.CompromissoSerializer

class CompromissoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Compromisso.objects.all()
    serializer_class = serializers.CompromissoSerializer
