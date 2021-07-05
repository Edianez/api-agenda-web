from rest_frameworks import serializers
from contato import models


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models
        fields = '__all__'