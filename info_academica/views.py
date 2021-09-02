from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import InfoAcademica
from .serializer import *

# Create your views here.
class InfoAcademicaAPIView(APIView):
    def get_queryset(self, queryUserId):
        if not queryUserId:
            return InfoAcademica.objects.all().prefetch_related("schedule_set", "academicgroup_set", "recreativeactivity_set")
        else:
            return InfoAcademica.objects.filter(idUser__exact=queryUserId).prefetch_related("schedule_set", "academicgroup_set", "recreativeactivity_set")

    def get(self, request):
        queryUserId = request.GET.get('userId')
        infoAcademicas = self.get_queryset(queryUserId)
        serializer = InfoAcademicaSerializer(infoAcademicas, many=True)
        return Response(serializer.data)
