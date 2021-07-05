from rest_frameworks import serializers
from contato import models


class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models
        fields