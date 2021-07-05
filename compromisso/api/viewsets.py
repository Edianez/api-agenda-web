from rest_framework import viewsets
from compromisso.api import serializers
from compromisso import models

class CompromissoViewSet(viewsets.ModelViewSet):
    serializers_class = serializers.CompromissoSerializer
    queryset = models.Compromisso.objects.all()

