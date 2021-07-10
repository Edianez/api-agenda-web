from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from apiagenda.contato.api.serializers import ContatoSerializer
from apiagenda.contato.models import Contato


class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome']
