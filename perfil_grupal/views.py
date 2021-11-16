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
sys.path.append('./model/PerfilGrupal')
sys.path.append('../')
import Constants
from perfil_grupal.model.PerfilGrupal import PerfilGrupal


'''
Servicio para obtener la información de perfiles grupales

endpoints:

	GET: Group

'''

class GroupAPIView(APIView):
    def get_queryset(self, queryUserId, queryGroupId):
        if not queryUserId and not queryGroupId:
            return Group.objects.all()
        else:
            return Group.objects.filter(Q(members__in=queryUserId) | Q(id__exact=queryUserId))

    '''
    DESCRIPTION: Indica la información de un grupo en específico.

    URL: http:///{{smartuj-endpoint}}/suj-s-009

    METHOD: GET

    QUERY PARAMS:
        GroupId: indica el grupo del cual se quiere recibir la información, si no se le paso el cluster
                devuelve la información de todos los clusters disponibles.
        UserId: indica el id del usuario del cual se quiere obtener el/los grupo/s a los que pertenece

    RESPONSE: Objeto GroupProfile

    '''
    def get(self, request):
        queryUserId = request.GET.get('userId')
        queryGroupId = request.GET.get('groupId')

        groupInfo = self.get_queryset(queryUserId, queryGroupId)
        serializer = GroupSerializer(groupInfo, many=True)
        return Response(serializer.data)


'''
Servicio para recibir el feedback de los usuarios

endpoints:

    GET: GroupFeedbackGet

	POST: GroupFeedbackPost

'''
class GroupFeedbackAPIView(APIView):
    def get_queryset(self, queryUserId, queryGroupId):
        if not queryUserId and not queryGroupId:
            return Group.objects.all().prefetch_related("recomendation_set")
        else:
            return Group.objects.filter(Q(members__in=queryUserId) | Q(id__exact=queryUserId)).prefetch_related("recomendation_set")


    '''
    DESCRIPTION: Devuelve estructuras que unen las recomendaciones, los usuarios y la calificación dada a la recomendación.

    URL: http:///{{smartuj-endpoint}}/suj-s-009/feedback

    METHOD: GET

    QUERY PARAMS:
        GroupId: indica el grupo del cual se quiere recibir la información, si
                 no se le paso el cluster devuelve la información de todos los clusters disponibles.
        UserId: indica el usuario del cual se quiere recibir la información.

    RESPONSE: Objeto GroupProfile

    '''
    def get(self, request):
        queryUserId = request.GET.get('userId')
        queryGroupId = request.GET.get('groupId')

        groupInfo = self.get_queryset(queryUserId, queryGroupId)
        serializer = GroupSerializer(groupInfo, many=True)
        return Response(serializer.data)

    '''
    DESCRIPTION: Guarda la recomendación dada al usuario, junto al ítem y la calificación dada por el usuario.

    URL: http:///{{smartuj-endpoint}}/suj-s-009/feedback

    METHOD: POST

    BODY:
        userId: IdUsuario para el cual se desea agregar el feedback

        itemId: id del ítem sobre el cual se genera el feedback

        score: indica la valoracion que se da a la recomendacion

    '''
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        # Se invoca el método para construir el feeback
        self.buildFeedback(body['itemId'], body['userId'], body['score'])

        return Response(status=202)

    '''
    Description: Función que se encarga de buscar los datos basados en el userId y
                    el itemId para agregarlo al dataframe de feedback

    Arguments:
        userId: IdUsuario para el cual se desea agregar el feedback

        itemId: id del ítem sobre el cual se genera el feedback

        score: indica la valoracion que se da a la recomendacion

    '''
    def buildFeedback(self, itemId, userId, score):

        # dataframe que contiene información de usuarios, préstamos y material
        df_join = PerfilGrupalConfig.lib_material.copy()

        # Para obtener datos del material
        by_item = df_join.loc[df_join['Llave'] == itemId].iloc[[0]]

        # Para obtener datos del usuario
        by_user = df_join.loc[df_join['IDUsuario'] == userId].iloc[[0]]

        # Para obtene el año en que se realiza el feedback
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")

        # Invocación a función para obtener el nivel del item recomendado al usuario
        nivel = self.nivelRec(userId, itemId)

        # Fila a guardar en el dataframe de feedback
        cell = {
            'RowID':by_item['RowID'].values[0],
            'Fecha':calendar.timegm(time.gmtime()),
            'IDItem':by_item['IDItem'].values[0],
            'Llave': itemId,
            'Programa':by_user['Programa'].values[0],
            'Facultad':by_user['Facultad'].values[0],
            'IDUsuario': userId,
            'Year': year,
            'Signatura':by_item['Signatura'].values[0],
            'Autor':by_item['Autor'].values[0],
            'Titulo':by_item['Titulo'].values[0],
            'AnioPublicacion':by_item['AnioPublicacion'].values[0],
            'DeweyUnidad':by_item['DeweyUnidad'].values[0],
            'DeweyDecena':by_item['DeweyDecena'].values[0],
            'DeweyCentena':by_item['DeweyCentena'].values[0],
            'Calificacion': score,
            'Nivel': nivel
        }


        PerfilGrupalConfig.lib_feedback = PerfilGrupalConfig.lib_feedback.append(cell, ignore_index=True)

        # Se sobre escribe el archivo almanecenado en dropbox para hacer uso del feeback recibido
        Constants.Constants.dbx.files_upload(
            str.encode(PerfilGrupalConfig.lib_feedback.to_json()),
            Constants.Constants.feedback_name,
            mode=dropbox.files.WriteMode.overwrite)

    '''
    Description: A partir del id de un usuario e id de un ítem se obtiene el nivel del ítem con respecto a las recomendaciones

    Arguments:
        userId: IdUsuario para el cual se desea agregar el feedback

        itemId: id del ítem sobre el cual se genera el feedback

    Return: nivel de un ítem para un usuario
    '''

    def nivelRec(self, userId, itemId):
        return PerfilGrupalConfig.lib_recommendations.loc[
                (PerfilGrupalConfig.lib_recommendations['IDUsuario'] == userId)
                    & (PerfilGrupalConfig.lib_recommendations['Llave'] == itemId), 'Nivel'].values[0]



'''
Servicio para entrenar el modelo de agrupación

endpoints:

    GET: ModelTrainer

'''

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
        print('Saving model')
        PerfilGrupalConfig.group_predictor.exportarDatos()

        return ''
