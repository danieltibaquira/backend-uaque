from rest_framework import serializers
from .models import UbicacionRed

class UbicacionRedSerializer(serializers.ModelSerializer):

    class Meta:
        model = UbicacionRed
        fields = "__all__"

