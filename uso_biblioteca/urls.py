from django.urls import path, include
from .views import LibUseAPIView
from .views import AzUseAPIView
from .views import RepoUseAPIView
from .views import LibResAPIView
from .views import AzResAPIView
from .views import RepoResAPIView

baseURL = 'suj-d-001'

urlpatterns = [
    path('suj-e-004/libUse', LibUseAPIView.as_view()),
    path('suj-e-004/azUse', AzUseAPIView.as_view()),
    path('suj-e-004/repoUse', RepoUseAPIView.as_view()),
    path('suj-e-004/libRes', LibResAPIView.as_view()),
    path('suj-e-004/azRes', AzResAPIView.as_view()),
    path('suj-e-004/repoRes', RepoResAPIView.as_view()),
]
