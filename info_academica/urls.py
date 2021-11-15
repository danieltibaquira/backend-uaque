from django.urls import path, include
from .views import InfoAcademicaAPIView

# URL Base para el servicio de info_academica
baseURL = 'suj-d-001'

# URLs registradas para el servicio
urlpatterns = [

    path('suj-d-001/', InfoAcademicaAPIView.as_view())

]
