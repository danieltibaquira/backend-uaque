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
import calendar
import time
import sys
import datetime
import dropbox
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

        self.buildFeedback(body['itemId'], body['userId'], body['score'])

        return Response(status=202)

    def buildFeedback(self, itemId, userId, score):
        df_join = PerfilGrupalConfig.lib_material.copy()

        by_item = df_join.loc[df_join['Llave'] == itemId].iloc[[0]]
        by_user = df_join.loc[df_join['IDUsuario'] == userId].iloc[[0]]

        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")

        cell = {
            'RowID':by_item['RowID'].values[0],
            'Fecha':calendar.timegm(time.gmtime()),
            'IDItem':by_item['IDItem'].values[0],
            'NumeroUbicacion':by_item['NumeroUbicacion'].values[0],
            'Dewey':by_item['Dewey'].values[0],
            'Ubicacion':by_item['Ubicacion'].values[0],
            'Llave': itemId,
            'Programa':by_user['Programa'].values[0],
            'Facultad':by_user['Facultad'].values[0],
            'IDUsuario': userId,
            'Year': year,
            'Signatura':by_item['Signatura'].values[0],
            'TipoItem':by_item['TipoItem'].values[0],
            'FechaCreacion':by_item['FechaCreacion'].values[0],
            'Autor':by_item['Autor'].values[0],
            'Titulo':by_item['Titulo'].values[0],
            'AnioPublicacion':by_item['AnioPublicacion'].values[0],
            'DeweyEspecifico':by_item['DeweyEspecifico'].values[0],
            'TemaDewey':by_item['TemaDewey'].values[0],
            'DeweyUnidad':by_item['DeweyUnidad'].values[0],
            'DeweyDecena':by_item['DeweyDecena'].values[0],
            'DeweyCentena':by_item['DeweyCentena'].values[0],
            'Temas':by_item['Temas'].values[0],
            'Union':by_item['Union'].values[0],
            'calificacion': score
        }

        print(cell)

        PerfilGrupalConfig.lib_feedback = PerfilGrupalConfig.lib_feedback.append(cell, ignore_index=True)

        PerfilGrupalConfig.dbx.files_upload(
            str.encode(PerfilGrupalConfig.lib_feedback.to_json()),
            '/feedback_users.json',
            mode=dropbox.files.WriteMode.overwrite)



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
