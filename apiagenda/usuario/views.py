from rest_framework import viewsets, renderers
from apiagenda.usuario.api.serializers import UsuarioSerializer
from apiagenda.usuario.models import Usuario
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

@csrf_exempt
def validate_login(request):
    if request.method == 'POST':
        body_data = json.loads(request.body)
        username = body_data['username']
        password = body_data['password']
        try:
            user = Usuario.objects.get(username=username, senha=password)
            if user is not None:
                return JsonResponse({'login': 'true'}, status=200)
            else:
                return JsonResponse({'error': 'Nome ou senha incorretos'}, status=400)
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Nome ou senha incorretos'}, status=400)
