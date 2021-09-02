from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from perfil_grupal.serializer import *
from perfil_grupal.models import Recommendation

class RecomemendationAPIView(APIView):
    def get_queryset(self, queryItemId, queryGroupId):
        if not queryItemId and not queryGroupId:
            return Recommendation.objects.all()
        else:
            return Recommendation.objects.filter(Q(itemId__exact=queryItemId) | Q(feedback__groupId__exact=queryGroupId))

    def get(self, request):
        queryItemId = request.GET.get('itemId')
        queryGroupId = request.GET.get('groupId')

        groupInfo = self.get_queryset(queryItemId, queryGroupId)
        serializer = RecomemendationSerializer(groupInfo, many=True)
        return Response(serializer.data)
