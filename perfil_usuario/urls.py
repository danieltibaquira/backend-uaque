from django.urls import path, include
from .views import AcademicInfoAPIView
from .views import BasicInfoAPIView
from .views import LibraryAPIView

baseURL = 'suj-d-001'

urlpatterns = [
    path('suj-s-003/users/academic', AcademicInfoAPIView.as_view()),
    path('suj-s-003/users/basicInfo', BasicInfoAPIView.as_view()),
    path('suj-s-003/users/lib', LibraryAPIView.as_view()),
]
