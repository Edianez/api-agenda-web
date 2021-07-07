from rest_framework import serializers
from contato import models


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contato
        fields = '__all__'

