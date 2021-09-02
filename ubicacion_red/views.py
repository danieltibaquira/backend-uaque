from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UbicacionRed
from .serializer import *

# Create your views here.
class UbicacionRedAPIView(APIView):
    def get_queryset(self, queryUserId):
        if not queryUserId:
            return UbicacionRed.objects.all()
        else:
            return UbicacionRed.objects.filter(idUser__exact=queryUserId)

    def get(self, request):
        queryUserId = request.GET.get('userId')
        ubicacionesRed = self.get_queryset(queryUserId)
        serializer = UbicacionRedSerializer(ubicacionesRed, many=True)
        return Response(serializer.data)
