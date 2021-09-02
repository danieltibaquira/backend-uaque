from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import InfoBasica
from .serializer import *

# Create your views here.
class InfoBasicaAPIView(APIView):
    def get_queryset(self, queryUserId):
        if not queryUserId:
            return InfoBasica.objects.all()
        else:
            return InfoBasica.objects.filter(idUser__exact=queryUserId)

    def get(self, request):
        queryUserId = request.GET.get('userId')
        infoBasicas = self.get_queryset(queryUserId)
        serializer = InfoBasicaSerializer(infoBasicas, many=True)
        return Response(serializer.data)
