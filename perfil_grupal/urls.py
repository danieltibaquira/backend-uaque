from django.urls import path, include
from .views import GroupAPIView
from .views import GroupFeedbackAPIView

baseURL = 'suj-d-001'

urlpatterns = [
    path('suj-s-009', GroupAPIView.as_view()),
    path('suj-s-009/feedback', GroupFeedbackAPIView.as_view()),
]
