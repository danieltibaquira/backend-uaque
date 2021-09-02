from rest_framework import serializers
from .models import InfoBasica

class InfoBasicaSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfoBasica
        fields = "__all__"

