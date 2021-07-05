from rest_frameworks import serializers
from usuario import models


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models
        fields