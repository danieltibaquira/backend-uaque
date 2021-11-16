from django.apps import AppConfig
import pandas as pd
import dropbox
import sys
sys.path.append('../')
import Constants

class PerfilGrupalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'perfil_grupal'

    # Dataframe que contiene la información del material biblográfico
    lib_material = pd.read_json(Constants.Constants.join)

    # Dataframe que contiene la información del feedback de los usuarios
    lib_feedback = pd.read_json(Constants.Constants.feedback)

    # Dataframe que contiene la información de las recomendaciones
    lib_recommendations = pd.read_json(Constants.Constants.recomendaciones)

    group_predictor = ''
