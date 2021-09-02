from django.urls import path, include
from .views import RecomemendationAPIView

baseURL = 'suj-d-001'

urlpatterns = [
    path('suj-i-009', RecomemendationAPIView.as_view()),
]
