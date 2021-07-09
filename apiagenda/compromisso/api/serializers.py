from rest_framework import serializers
from apiagenda.compromisso import models


class CompromissoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Compromisso
        fields = '__all__'

