from django.urls import path, include
from .views import GroupAPIView
from .views import GroupFeedbackAPIView
from .views import ModelTrainerAPIView

# URL Base para el servicio de perfil grupal: suj-s-009

urlpatterns = [
    # URLs registradas para el servicio
    path('suj-s-009', GroupAPIView.as_view()),
    path('suj-s-009/feedback', GroupFeedbackAPIView.as_view()),
    path('suj-s-009/model', ModelTrainerAPIView.as_view()),

]
