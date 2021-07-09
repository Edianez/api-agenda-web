from rest_framework import viewsets, renderers
from apiagenda.usuario.api.serializers import UsuarioSerializer
from apiagenda.usuario.models import Usuario


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
