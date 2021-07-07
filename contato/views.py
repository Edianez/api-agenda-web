from rest_framework import generics
from contato.api import serializers
from contato import models


class ContatoList(generics.ListCreateAPIView):
    queryset = models.Contato.objects.all()
    serializer_class = serializers.ContatoSerializer

class ContatoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Contato.objects.all()
    serializer_class = serializers.ContatoSerializer
