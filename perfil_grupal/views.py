from django.shortcuts import render
from django.db.models import Q
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from perfil_grupal.models import Group
from perfil_grupal.models import Feedback
from perfil_grupal.models import Recommendation
from .apps import PerfilGrupalConfig
import sys
sys.path.append('./model/PerfilGrupal')
from perfil_grupal.model.PerfilGrupal import PerfilGrupal

class GroupAPIView(APIView):
    def get_queryset(self, queryUserId, queryGroupId):
        if not queryUserId and not queryGroupId:
            return Group.objects.all()
        else:
            return Group.objects.filter(Q(members__in=queryUserId) | Q(id__exact=queryUserId))

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
            return Group.objects.filter(Q(members__in=queryUserId) | Q(id__exact=queryUserId)).prefetch_related("recomendation_set")

    def get(self, request):
        queryUserId = request.GET.get('userId')
        queryGroupId = request.GET.get('groupId')

        groupInfo = self.get_queryset(queryUserId, queryGroupId)
        serializer = GroupSerializer(groupInfo, many=True)
        return Response(serializer.data)

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        feed = Feedback.objects.create(
            groupId=body['groupId']
        )

        Recommendation.objects.create(
            itemId=body['itemId'],
            userId=body['userId'],
            score=body['score'],
            feedback=feed
        )

        return Response(status=202)

class ModelTrainerAPIView(APIView):
    def get(self, request):
        print('Initializing Model')
        PerfilGrupalConfig.group_predictor = PerfilGrupal()
        print('Creating weights')
        PerfilGrupalConfig.group_predictor.crearPeso()
        print('Creating tables')
        PerfilGrupalConfig.group_predictor.invocarTablaPesos()
        print('Normalizing')
        PerfilGrupalConfig.group_predictor.invocarNormalizarPesos()
        print('Making groups')
        PerfilGrupalConfig.group_predictor.invocarClustering()

        return ''
