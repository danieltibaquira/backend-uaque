from rest_framework import serializers
from .models import UbicacionRed

# Objetos serializadores para las respuestas de los endpoints
class UbicacionRedSerializer(serializers.ModelSerializer):

    class Meta:
        model = UbicacionRed
        fields = "__all__"

