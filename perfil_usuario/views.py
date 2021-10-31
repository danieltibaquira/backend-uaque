from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AcademicInfo
from .models import TermSummary
from .models import Classes
from .models import BasicInfo
from .models import LibraryHistory
from .models import TransactionLibrary
from .serializer import *

# Create your views here.
class AcademicInfoAPIView(APIView):
    def get_queryset(self, queryUserId, queryDateStart, queryDateEnd, queryTermSum, queryClasses):
        if not queryUserId and not queryDateStart and not queryDateEnd:
            return AcademicInfo.objects.all().prefetch_related("termsummary_set", "classes_set")
        else:
            return AcademicInfo.objects.filter(idUser__exact=queryUserId).prefetch_related("termsummary_set", "classes_set")

    def get(self, request):
        queryUserId = request.GET.get('userId')
        queryDateStart = request.GET.get('dateStart')
        queryDateEnd = request.GET.get('dateEnd')
        queryTermSum = request.GET.get('termSummaries')
        queryClasses = request.GET.get('classes')

        infoAcademicas = self.get_queryset(queryUserId, queryDateStart, queryDateEnd, queryTermSum, queryClasses)
        serializer = AcademicInfoSerializer(infoAcademicas, many=True)
        return Response(serializer.data)

class BasicInfoAPIView(APIView):
    def get_queryset(self, queryUserId):
        if not queryUserId:
            return BasicInfo.objects.all()
        else:
            return BasicInfo.objects.filter(idUser__exact=queryUserId)

    def get(self, request):
        queryUserId = request.GET.get('userId')

        infoBasicas = self.get_queryset(queryUserId)
        serializer = BasicInfoSerializer(infoBasicas, many=True)
        return Response(serializer.data)

class LibraryAPIView(APIView):
    def get_queryset(self, queryUserId, queryDateStart, queryDateEnd, queryFaculty):
        if not queryUserId and not queryDateStart and not queryDateEnd:
            return LibraryHistory.objects.all().prefetch_related("transactionlibrary_set")
        else:
            return LibraryHistory.objects.filter(idUser__exact=queryUserId).prefetch_related("transactionlibrary_set")

    def get(self, request):
        queryUserId = request.GET.get('userId')
        queryDateStart = request.GET.get('dateStart')
        queryDateEnd = request.GET.get('dateEnd')
        queryFaculty = request.GET.get('faculty')

        lib = self.get_queryset(queryUserId, queryDateStart, queryDateEnd, queryFaculty)
        serializer = LibraryHistorySerializer(lib, many=True)
        return Response(serializer.data)


