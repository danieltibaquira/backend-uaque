from django.shortcuts import render
from .serializer import *

# localizacion/views.py
from django.shortcuts import render

def locMinExample(request):
    return render(request, 'localizacion/locMinExample.html', {})
