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

import plotly.express as px

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

class DashboardFeedback(APIView):
    def get(self, request):
        dewey = request.GET.get('dewey')
        dewey_unit = request.GET.get('dewey_unit')
        #Traemos todas las llaves con susu deweys de todas las unidades
        all_deweys = pd.DataFrame(UsoBibliotecaConfig.lib_material[['DeweyUnidad', 'DeweyDecena', 'DeweyCentena', 'Llave']].drop_duplicates())

        #Join entre las dos tablas desde la Llave del libro
        reviewed_books: pd.DataFrame = UsoBibliotecaConfig.lib_feedback.merge(all_deweys, on='Llave', suffixes=('_feedback', '_all_deweys'))
        reviewed_books = pd.DataFrame(reviewed_books.drop_duplicates(subset=['IDUsuario', 'Calificacion', 'Llave']))
        dewey_unit_name = self.level_to_dewey_option(dewey_unit)
        if not dewey_unit_name == 'BC' and not dewey_unit_name == 'Nuevo':
            selected_row: pd.DataFrame = reviewed_books.loc[(reviewed_books['Nivel'] == float(dewey_unit)) & (reviewed_books[dewey_unit_name]== int(dewey))]
        else:
            selected_row: pd.DataFrame  = reviewed_books.loc[(reviewed_books['Nivel'] == dewey_unit) ]
        return Response(selected_row)


    #Dado un valor numerico de dewey, se devuelve el nombre de ese valor
    def level_to_dewey_option(self, selected_dewey_level):
        if selected_dewey_level == "0.5":
            selected_dewey_option = 'DeweyUnidad'
        elif selected_dewey_level == "0.2":
            selected_dewey_option = 'DeweyDecena'
        elif selected_dewey_level == "0.1":
            selected_dewey_option = 'DeweyCentena'
        elif selected_dewey_level == "BC":
            selected_dewey_option = 'BC'
        elif selected_dewey_level == "Nuevo":
            selected_dewey_option = 'BC'
        else:
            selected_dewey_option = 'DeweyUnidad'
        return selected_dewey_option

class DashboardFeedbackUtilsDeweyList(APIView):
    def get(self, request):
        selected_dewey_level = request.GET.get('selected_dewey_level')


        #Join entre las dos tablas desde la Llave del libro
        all_deweys = pd.DataFrame(UsoBibliotecaConfig.lib_material[['DeweyUnidad', 'DeweyDecena', 'DeweyCentena', 'Llave']])
        reviewed_books: pd.DataFrame = UsoBibliotecaConfig.lib_feedback.merge(all_deweys, on='Llave', suffixes=('_feedback', '_all_deweys'))
        reviewed_books = pd.DataFrame(reviewed_books.drop_duplicates(subset=['IDUsuario', 'Calificacion', 'Llave']))
        selected_dewey_option = self.level_to_dewey_option(selected_dewey_level)

        if not selected_dewey_option == 'BC' and not selected_dewey_option == 'Nuevo':
            dewey_list = reviewed_books[selected_dewey_option].unique()
            dewey_list = [{"label": x, "value": x } for x in dewey_list]
        else:
            dewey_list=[]
        return Response(dewey_list)

    #Dado un valor numerico de dewey, se devuelve el nombre de ese valor
    def level_to_dewey_option(self, selected_dewey_level):
        if selected_dewey_level == "0.5":
            selected_dewey_option = 'DeweyUnidad'
        elif selected_dewey_level == "0.2":
            selected_dewey_option = 'DeweyDecena'
        elif selected_dewey_level == "0.1":
            selected_dewey_option = 'DeweyCentena'
        elif selected_dewey_level == "BC":
            selected_dewey_option = 'BC'
        elif selected_dewey_level == "Nuevo":
            selected_dewey_option = 'BC'
        else:
            selected_dewey_option = 'DeweyUnidad'
        return selected_dewey_option

class DashboardGrupos(APIView):
    def get(self, request):
        dewey = request.GET.get('dewey')

        table_columns = ['nombre_usuario', 'email','IDUsuario', 'Facultad', 'Programa']
        users_info = UsoBibliotecaConfig.lib_material[['IDUsuario', 'Facultad', 'Programa','DeweyUnidad', 'DeweyDecena', 'DeweyCentena']]
        users_info = users_info.drop_duplicates(subset=['IDUsuario', 'Facultad', 'Programa'])
        users_info = users_info.merge(UsoBibliotecaConfig.lib_pesos_usuarios, on='IDUsuario')
        fake_users_info = UsoBibliotecaConfig.lib_fake_user_info

        threshold = 0.2
        if dewey == -999:
            dewey = "-999"
        does_dewey_match = users_info[str(dewey)] >= threshold
        selected_rows = users_info.loc[does_dewey_match]
        selected_rows = selected_rows[['IDUsuario', 'Facultad', 'Programa']]
        #insert mock data
        n_rows = len(selected_rows.index)
        if n_rows>len(fake_users_info.index):
            n_rows = len(fake_users_info.index)
        fake_info = fake_users_info.sample(n=n_rows)
        selected_rows = pd.concat([selected_rows.reset_index(),fake_info.reset_index()], axis=1)
        response = selected_rows[table_columns].to_dict('records')
        return Response(response)


class DashboardGruposUtilsDeweyList(APIView):
    def get(self, request):
        selected_dewey_level = request.GET.get('selected_dewey_level')


        all_deweys = pd.DataFrame(UsoBibliotecaConfig.lib_material[['DeweyUnidad', 'DeweyDecena', 'DeweyCentena']])

        dewey_list = []
        selected_dewey_option = self.level_to_dewey_option(selected_dewey_level)

        dewey_list = all_deweys[selected_dewey_option].unique()
        dewey_list = [{"label": x, "value": x } for x in dewey_list]

        return Response(dewey_list)

    #Dado un valor numerico de dewey, se devuelve el nombre de ese valor
    def level_to_dewey_option(self, selected_dewey_level):
        if selected_dewey_level == "0.5":
            selected_dewey_option = 'DeweyUnidad'
        elif selected_dewey_level == "0.2":
            selected_dewey_option = 'DeweyDecena'
        elif selected_dewey_level == "0.1":
            selected_dewey_option = 'DeweyCentena'
        elif selected_dewey_level == "BC":
            selected_dewey_option = 'BC'
        elif selected_dewey_level == "Nuevo":
            selected_dewey_option = 'BC'
        else:
            selected_dewey_option = 'DeweyUnidad'
        return selected_dewey_option
