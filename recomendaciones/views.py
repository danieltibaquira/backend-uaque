from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from perfil_grupal.serializer import *
from perfil_grupal.models import Recommendation
import pandas as pd
from surprise import Dataset
from surprise import Reader
import surprise.dump
import sys
sys.path.append('./model/Recommendaciones')
from recomendaciones.model.Recomendaciones import Recomendaciones
from os.path import dirname, join
import json
from .apps import RecomendacionesConfig
import math
import numpy as np


class RecomemendationAPIView(APIView):
    def get_queryset(self, queryItemId, queryGroupId):
        if not queryItemId and not queryGroupId:
            return Recommendation.objects.all()
        else:
            # return Recommendation.objects.filter(Q(itemId__exact=queryItemId) | Q(feedback__groupId__exact=queryGroupId))
            return self.generateRecomendations(queryGroupId)

    def get(self, request):
        queryItemId = request.GET.get('itemId')
        queryGroupId = request.GET.get('groupId')

        # groupInfo = self.get_queryset(queryItemId, queryGroupId)
        # serializer = RecomemendationSerializer(groupInfo, many=True)
        print("Recibo request")
        recs = self.generateRecomendations(queryGroupId)
        print("Recomendaciones listas y respondiendo")
        return Response(recs)


    def generateRecomendations(self, cluster):
        print("Computando recomendaciones")
        data_recs_asr = self.recomendaciones_usuario(cluster)
        print("IDs a recomendar", data_recs_asr)
        final_recs = []
        for ids in data_recs_asr:
            final_recs.append(self.itemIdToMaterial(ids))

        print("Recomendaciones finales", final_recs)
        return final_recs

    def recomendaciones_usuario(self,  id_usuario):
        df_recomendaciones = RecomendacionesConfig.lib_recommendations.copy()

        recomendaciones_u = df_recomendaciones.loc[df_recomendaciones["IDUsuario"] == id_usuario]

        return recomendaciones_u['Llave'].values


    def itemIdToMaterial(self, itemId):
        print("Calculando id a titulo")
        found = (RecomendacionesConfig.lib_material.loc[RecomendacionesConfig.lib_material['Llave'] == itemId])
        found_title = found['Titulo'].values[0]
        found_location = found['Signatura'].values[0]
        found_author = found['Autor'].values[0]
        found_dewey = found['Dewey'].values[0]

        tematicas = RecomendacionesConfig.lib_themes.loc[
            RecomendacionesConfig.lib_themes['Llaves'] == str(itemId)
            ]['Tema 670'].values
        return {
            'itemId':(itemId),
            'title': found_title,
            'location': found_location,
            'author': found_author,
            'userId': itemId,
            'dewey': found_dewey,
            'themes': tematicas
        }

    def itemIdToLocation(self, itemId):
        print("Calculando id a signatura")
        found = (RecomendacionesConfig.lib_material.loc[
            RecomendacionesConfig.lib_material['Llave'] == itemId
            ]['Signatura'].unique())
        if len(found) > 0:
           return found[0]
        else:
            return ''

    def itemIdToAuthor(self, itemId):
        print("Calculando id a autor")
        found = (RecomendacionesConfig.lib_material.loc[
            RecomendacionesConfig.lib_material['Llave'] == itemId
            ]['Autor'].unique())
        if len(found) > 0:
           return found[0]
        else:
            return ''

    def itemIdToDewey(self, itemId):
        print("Calculando id a dewey")
        found = (RecomendacionesConfig.lib_material.loc[
            RecomendacionesConfig.lib_material['Llave'] == itemId
            ]['Dewey'].unique())
        if len(found) > 0:
           return found[0]
        else:
            return ''

    def itemIdToThemes(self, itemId):
        print("Calculando id a temas")
        tematicas = RecomendacionesConfig.lib_themes.loc[
            RecomendacionesConfig.lib_themes['Llaves'] == str(itemId)
            ]['Tema 670'].values
        if len(tematicas) == 0:
            return []
        else:
            return tematicas

class ModelTrainerAPIView(APIView):
    def get(self, request):
        RecomendacionesConfig.recommendation_predictor = Recomendaciones()
        RecomendacionesConfig.recommendation_predictor.crearPesos()
        RecomendacionesConfig.recommendation_predictor.cargarModelo()
        RecomendacionesConfig.recommendation_predictor.invocarCalculoLista()
        RecomendacionesConfig.recommendation_predictor.invocarRecomendaciones()
        RecomendacionesConfig.recommendation_predictor.invocarRecomendacionesLibrosNuevos()
        RecomendacionesConfig.recommendation_predictor.unionRecomendaciones()
        RecomendacionesConfig.recommendation_predictor.invocarFiltrarRecomendaciones()
        RecomendacionesConfig.recommendation_predictor.unionRecomendacionesFinales()
        RecomendacionesConfig.recommendation_predictor.unionRecomendacionesFinales()
        RecomendacionesConfig.recommendation_predictor.exportarRecomendaciones()

        return ''
