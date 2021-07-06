from rest_framework import serializers
from compromisso import models


class CompromissoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Compromisso
        fields = '__all__'

