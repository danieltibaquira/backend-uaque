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

'''
Servicio para obtener el feedback

endpoints:

	GET: Recommendation

'''

class RecomemendationAPIView(APIView):

    '''
    DESCRIPTION: Retorna la lista de recomendaciones para un grupo en especifico

    URL: http:///{{smartuj-endpoint}}/suj-i-009

    METHOD: GET

    QUERY PARAMS:
        UserId: El id del grupo señala el grupo sobre el cual se retornarán las recomendaciones.
                Si no se proporciona un Id se devuelve el conjunto(arreglo) de todos los recursos.

    RESPONSE: Lista de recomendaciones

    '''
    def get(self, request):
        queryGroupId = request.GET.get('groupId')

        # Se invoca la función que obtiene las recomendaciones a partir del id del grupo
        recs = self.generateRecomendations(queryGroupId)
        return Response(recs)


    '''
    Description: Utilizando el dataset de recomendaciones y el id del grupo buscamos las top 10 recomendaciones

    Arguments: cluster -> identificador del grupo

    Return: lista de recomendaciones

    '''
    def generateRecomendations(self, cluster):

        # Invocamos la función que obtiene los ids de los ítems a recomendar
        data_recs_asr = self.recomendaciones_usuario(cluster)
        final_recs = []

        # Llenamos el array con el diccionario de la información para cada ítem a recomendar
        for ids in data_recs_asr:
            final_recs.append(self.itemIdToMaterial(ids))

        print("Recomendaciones finales", final_recs)
        return final_recs

    '''
    Description: Utilizando el dataset de recomendaciones y el id del grupo buscamos los ids para el top 10 recomendaciones

    Arguments: id_usuario -> identificador del usuario al cual se realiza la recomendación

    Return: lista de ids de ítems

    '''
    def recomendaciones_usuario(self,  id_usuario):
        df_recomendaciones = RecomendacionesConfig.lib_recommendations.copy()

        # Buscamos en el dataframe de recomendaciones aquellas que corresponder al id del usuario a evaluar
        recomendaciones_u = df_recomendaciones.loc[df_recomendaciones["IDUsuario"] == id_usuario]

        return recomendaciones_u['Llave'].values


    '''
    Description: Función que construye la información de un ítem

    Arguments: itemId -> identificador del ítem que se está construyendo

    Return: diccionario con la información del ítem

    '''
    def itemIdToMaterial(self, itemId):
        print("Calculando id a titulo")

        # Para obtener toda la información del ítem
        found = (RecomendacionesConfig.lib_material.loc[RecomendacionesConfig.lib_material['Llave'] == itemId])

        # Para obtener el título del ítem
        found_title = found['Titulo'].values[0]

        # Para obtener la ubicación del ítem
        found_location = found['Signatura'].values[0]

        # Para obtener el autor del ítem
        found_author = found['Autor'].values[0]

        # Para obtener el dewey del ítem
        found_dewey = found['Dewey'].values[0]

        # Para obtener las temáticas del ítem
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


'''
Servicio para entrenar el modelo de recomendación

endpoints:

	GET: ModelTrainer

'''
class ModelTrainerAPIView(APIView):

    '''
    DESCRIPTION: Entrena el modelo de recomendaciones

    URL: http:///{{smartuj-endpoint}}/suj-i-009/model

    METHOD: GET

    '''
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
