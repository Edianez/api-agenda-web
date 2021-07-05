from rest_frameworks import serializers
from compromisso import models


class CompromissoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models
        fields = '__all__'