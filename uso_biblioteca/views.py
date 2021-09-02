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

# Create your views here.
class LibUseAPIView(APIView):
    def get_queryset(self, queryUserId):
        if not queryUserId:
            return LibUse.objects.all().prefetch_related("tranlib_set")
        else:
            return LibUse.objects.filter(idUser__exact=queryUserId).prefetch_related("tranlib_set")

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

    def get(self, request):
        queryUserId = request.GET.get('userId')
        repoUses = self.get_queryset(queryUserId)
        serializer = RepoUseSerializer(repoUses, many=True)
        return Response(serializer.data)

class LibResAPIView(APIView):
    def get_queryset(self, queryItemId):
        if not queryItemId:
            return LibRes.objects.all()
        else:
            return LibRes.objects.filter(idResource__exact=queryItemId)

    def get(self, request):
        queryItemId = request.GET.get('itemId')
        libResources = self.get_queryset(queryItemId)
        serializer = LibResSerializer(libResources, many=True)
        return Response(serializer.data)

class AzResAPIView(APIView):
    def get_queryset(self, queryItemId):
        if not queryItemId:
            return AzRes.objects.all()
        else:
            return AzRes.objects.filter(idResource__exact=queryItemId)

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

    def get(self, request):
        queryItemId = request.GET.get('itemId')
        repoResources = self.get_queryset(queryItemId)
        serializer = RepoResSerializer(repoResources, many=True)
        return Response(serializer.data)
