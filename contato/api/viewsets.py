from rest_framework import viewsets
from contato.api import serializers
from contato import models

class ContatoViewSet(viewsets.ModelViewSet):
    serializers_class = serializers.ContatoSerializer
    queryset = models.Contato.objects.all()

