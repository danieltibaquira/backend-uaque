"""uaque URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', include('info_academica.urls')),
    #path('api/', include('info_basica.urls')),
    path('api/', include('ubicacion_red.urls')),
    #path('api/', include('uso_biblioteca.urls')),
    #path('api/', include('perfil_usuario.urls')),
    #path('api/', include('perfil_grupal.urls')),
    #path('api/', include('recomendaciones.urls')),
    path('api/', include('localizacion.urls')),
]
