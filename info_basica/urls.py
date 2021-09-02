from django.urls import path, include
from .views import InfoBasicaAPIView


urlpatterns = [
    path('suj-d-003/', InfoBasicaAPIView.as_view())
]
