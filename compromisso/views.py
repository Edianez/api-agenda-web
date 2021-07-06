from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from compromisso.api import serializers
from compromisso import models


@csrf_exempt
def compromisso_list(request):
    if request.method == 'GET':
        compromissos = models.Compromisso.objects.all()
        serializer = serializers.CompromissoSerializer(compromissos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.CompromissoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def compromisso_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        compromisso = models.Compromisso.objects.get(pk=pk)
    except models.Compromisso.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = serializers.CompromissoSerializer(compromisso)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = serializers.CompromissoSerializer(compromisso, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        compromisso.delete()
        return HttpResponse(status=204)
