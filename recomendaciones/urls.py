from django.urls import path, include
from .views import RecomemendationAPIView
from .views import ModelTrainerAPIView

baseURL = 'suj-d-001'

urlpatterns = [
    path('suj-i-009', RecomemendationAPIView.as_view()),
    path('suj-i-009/model', ModelTrainerAPIView.as_view()),
]
