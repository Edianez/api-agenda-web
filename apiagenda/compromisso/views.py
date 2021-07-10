from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from apiagenda.compromisso.api.serializers import CompromissoSerializer
from apiagenda.compromisso.models import Compromisso


class CompromissoViewSet(viewsets.ModelViewSet):
    serializer_class = CompromissoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['idcontato']

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Compromisso.objects.all()
        data_inicio = self.request.query_params.get('data_inicio')
        data_fim = self.request.query_params.get('data_fim')
        if (data_inicio is not None) and (data_fim is not None):
            queryset = Compromisso.objects.filter(data__range=[data_inicio, data_fim])
        return queryset
