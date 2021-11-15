from django.urls import path, include
from .views import InfoBasicaAPIView

# URL Base para el servicio: suj-d-003/
urlpatterns = [
    # URLs registradas para el servicio
    path('suj-d-003/', InfoBasicaAPIView.as_view())

]
