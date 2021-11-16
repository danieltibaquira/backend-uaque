from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import LibUse
from .models import AzUse
from .models import RepoUse
from .models import LibRes
from .models import AzRes
from .models import RepoRes
from .serializer import *
import pandas as pd
from .apps import UsoBibliotecaConfig
import sys
sys.path.append('./DataPrep/DataPrep')
sys.path.append('../')
import Constants
from uso_biblioteca.DataPrep.DataPrep import Material
from uso_biblioteca.DataPrep.DataPrep import History
from uso_biblioteca.DataPrep.DataPrep import Merger


# Create your views here.
class LibUseAPIView(APIView):
    def get_queryset(self, queryUserId):
        if not queryUserId:
            return LibUse.objects.all().prefetch_related("tranlib_set")
        else:
            return LibUse.objects.filter(idUser__exact=queryUserId).prefetch_related("tranlib_set")

    '''
    DESCRIPTION: Servicio que expone las transacciones realizados por un usuario sobre material bibliográfico de la biblioteca.

    URL: http:///{{smartuj-endpoint}}/suj-e-004/libUse

    METHOD: GET

    QUERY PARAMS:
        userId: Id del usuario para el cual se desea encontrar la información del uso de la biblioteca.

    RESPONSE: Objeto LibUse

    '''
    def get(self, request):
        queryUserId = request.GET.get('userId')
        libUses = self.get_queryset(queryUserId)
        serializer = LibUseSerializer(libUses, many=True)
        return Response(serializer.data)

class AzUseAPIView(APIView):
    def get_queryset(self, queryUserId):
        if not queryUserId:
            return AzUse.objects.all().prefetch_related("tranaz_set")
        else:
            return AzUse.objects.filter(idUser__exact=queryUserId).prefetch_related("tranaz_set")

    '''
    DESCRIPTION: Servicio que indica los recursos consultados de recursos electrónicos AZ por parte de los estudiantes.

    URL: http:///{{smartuj-endpoint}}/suj-e-004/azUse

    METHOD: GET

    QUERY PARAMS:
        userId: Id del usuario para el cual se desea encontrar la información del uso de la biblioteca.

    RESPONSE: Objeto AzUse

    '''
    def get(self, request):
        queryUserId = request.GET.get('userId')
        azUses = self.get_queryset(queryUserId)
        serializer = AzUseSerializer(azUses, many=True)
        return Response(serializer.data)

class RepoUseAPIView(APIView):
    def get_queryset(self, queryUserId):
        if not queryUserId:
            return RepoUse.objects.all().prefetch_related("tranrepo_set")
        else:
            return RepoUse.objects.filter(idUser__exact=queryUserId).prefetch_related("tranrepo_set")

    '''
    DESCRIPTION: Servicio que indica las transacciones realizadas por un usuario en el repositorio institucional.

    URL: http:///{{smartuj-endpoint}}/suj-e-004/repoUse

    METHOD: GET

    QUERY PARAMS:
        userId: Id del usuario para el cual se desea encontrar la información del uso de la biblioteca.

    RESPONSE: Objeto RepoUse

    '''
    def get(self, request):
        queryUserId = request.GET.get('userId')
        repoUses = self.get_queryset(queryUserId)
        serializer = RepoUseSerializer(repoUses, many=True)
        return Response(serializer.data)

class LibResAPIView(APIView):
    df_material = UsoBibliotecaConfig.lib_material.copy()


    '''
    DESCRIPTION: Servicio que entrega información sobre material Bibliográfico físico de la biblioteca.

    URL: http:///{{smartuj-endpoint}}/suj-e-004/libRes

    METHOD: GET

    QUERY PARAMS:
    itemId: Id del recurso de la biblioteca para el cual se desea obtener información.
            Si no se proporciona un Id se devuelve el conjunto(arreglo) de todos los recursos

    RESPONSE: Objeto LibRes

    '''
    def get(self, request):
        queryItemId = request.GET.get('itemId')
        found_titles = self.df_material.loc[self.df_material['Titulo'].str.lower().str.contains(str(queryItemId).lower())]
        titles_res = []
        for index, row in found_titles.iterrows():
            titles_res.append({
                'itemId': row['Llave'],
                'title': row['Titulo'],
                'autor': row['Autor'],
                'year': row['AnioPublicacion']
            })
        return Response(titles_res)

class AzResAPIView(APIView):
    def get_queryset(self, queryItemId):
        if not queryItemId:
            return AzRes.objects.all()
        else:
            return AzRes.objects.filter(idResource__exact=queryItemId)

    '''
    DESCRIPTION: Servicio que indica las transacciones realizadas por un usuario en el repositorio institucional.

    URL: http:///{{smartuj-endpoint}}/suj-e-004/azRes

    METHOD: GET

    QUERY PARAMS:
    itemId: Id del recurso de la biblioteca para el cual se desea obtener información.
            Si no se proporciona un Id se devuelve el conjunto(arreglo) de todos los recursos

    RESPONSE: Objeto AzRes

    '''
    def get(self, request):
        queryItemId = request.GET.get('itemId')
        azResources = self.get_queryset(queryItemId)
        serializer = AzResSerializer(azResources, many=True)
        return Response(serializer.data)

class RepoResAPIView(APIView):
    def get_queryset(self, queryItemId):
        if not queryItemId:
            return RepoRes.objects.all()
        else:
            return RepoRes.objects.filter(idResource__exact=queryItemId)

    '''
    DESCRIPTION: Servicio que entrega la información de los recursos disponibles en el repositorio institucional.

    URL: http:///{{smartuj-endpoint}}/suj-e-004/repoRes

    METHOD: GET

    QUERY PARAMS:
    itemId: Id del recurso de la biblioteca para el cual se desea obtener información.
            Si no se proporciona un Id se devuelve el conjunto(arreglo) de todos los recursos

    RESPONSE: Objeto repoRes

    '''
    def get(self, request):
        queryItemId = request.GET.get('itemId')
        repoResources = self.get_queryset(queryItemId)
        serializer = RepoResSerializer(repoResources, many=True)
        return Response(serializer.data)

class DataPrepAPIView(APIView):
    def get(self, request):
        prepM = Material()
        prepM.clean()
        prepH = History()
        prepH.clean()
        merger = Merger(prepH, prepM)
        merger.join()

        return Response(status=202)
