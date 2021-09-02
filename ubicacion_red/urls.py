from django.urls import path, include
from .views import UbicacionRedAPIView


urlpatterns = [
    path('suj-e-001/', UbicacionRedAPIView.as_view())
]
