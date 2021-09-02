from rest_framework import serializers
from .models import Group
from .models import Feedback
from .models import Recommendation

class GroupSerializer(serializers.Serializer):
    class Meta:
        model = Group
        fields ='__all__'

class RecomemendationSerializer(serializers.Serializer):
    class Meta:
        model = Recommendation
        fields ='__all__'

class FeedbackSerializer(serializers.Serializer):
    recomendations = RecomemendationSerializer(read_only=True, source='recomendation_set', many=True)
    class Meta:
        model = Feedback
        fields ='__all__'
