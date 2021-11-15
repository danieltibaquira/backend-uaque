from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import InfoBasica
from .serializer import *


'''
Servicio para obtener información básica de los usuarios

endpoints:

    GET: InfoBasica

'''
class InfoBasicaAPIView(APIView):
    def get_queryset(self, queryUserId):
        if not queryUserId:
            return InfoBasica.objects.all()
        else:
            return InfoBasica.objects.filter(idUser__exact=queryUserId)

    '''
    DESCRIPTION: Retorna los datos básicos de los usuarios.

    URL: http:///{{smartuj-endpoint}}/suj-d-003/

    METHOD: GET

    QUERY PARAMS: userId
    Description: IdUsuario indica el usuario del cual se quiere recibir la información,
    si no se proporciona un id se retorna un conjunto (arreglo) de los datos básicos
    de todos los miembros de la comunidad académica usuarios del sistema.

    RESPONSE: Objeto InfoAcademica

    '''
    def get(self, request):
        queryUserId = request.GET.get('userId')
        infoBasicas = self.get_queryset(queryUserId)
        serializer = InfoBasicaSerializer(infoBasicas, many=True)
        return Response(serializer.data)
