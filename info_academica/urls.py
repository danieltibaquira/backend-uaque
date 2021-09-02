from django.urls import path, include
from .views import InfoAcademicaAPIView

baseURL = 'suj-d-001'

urlpatterns = [
    path('suj-d-001/', InfoAcademicaAPIView.as_view())
]
