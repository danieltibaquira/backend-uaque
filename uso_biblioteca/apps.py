from django.apps import AppConfig
import pandas as pd
import sys
sys.path.append('../')
import Constants


class UsoBibliotecaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'uso_biblioteca'

    lib_material = pd.read_json(Constants.Constants.join)
