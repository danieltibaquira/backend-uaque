from django.shortcuts import render
from django.db.models import Q
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from perfil_grupal.models import Group
from perfil_grupal.models import Feedback
from perfil_grupal.models import Recommendation

class GroupAPIView(APIView):
    def get_queryset(self, queryUserId, queryGroupId):
        if not queryUserId and not queryGroupId:
            return Group.objects.all()
        else:
            return Group.objects.filter(Q(members__in=queryUserId) | Q(id__exact=queryGroupId))

    def get(self, request):
        queryUserId = request.GET.get('userId')
        queryGroupId = request.GET.get('groupId')

        groupInfo = self.get_queryset(queryUserId, queryGroupId)
        serializer = GroupSerializer(groupInfo, many=True)
        return Response(serializer.data)


class GroupFeedbackAPIView(APIView):
    def get_queryset(self, queryUserId, queryGroupId):
        if not queryUserId and not queryGroupId:
            return Group.objects.all().prefetch_related("recomendation_set")
        else:
            return Group.objects.filter(Q(members__in=queryUserId) | Q(id__exact=queryGroupId)).prefetch_related("recomendation_set")

    def get(self, request):
        queryUserId = request.GET.get('userId')
        queryGroupId = request.GET.get('groupId')

        groupInfo = self.get_queryset(queryUserId, queryGroupId)
        serializer = GroupSerializer(groupInfo, many=True)
        return Response(serializer.data)

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        '''
        feed = Feedback.objects.create(
            groupId=body['groupId']
        )

        Recommendation.objects.create(
            itemId=body['itemId'],
            userId=body['userId'],
            score=body['score'],
            feedback=feed
        )
        '''
        Recommendation.objects.create(
            itemId=body['itemId'],
            userId=body['userId'],
            score=body['score'],
            groupId=body['groupId']
        )

        return Response(status=202)
