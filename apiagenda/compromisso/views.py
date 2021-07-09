from rest_framework import viewsets
from apiagenda.compromisso.api.serializers import CompromissoSerializer
from apiagenda.compromisso.models import Compromisso


class CompromissoViewSet(viewsets.ModelViewSet):
    queryset = Compromisso.objects.all()
    serializer_class = CompromissoSerializer
