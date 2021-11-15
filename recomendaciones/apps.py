from django.apps import AppConfig
import html
from pathlib import Path
import os
import gzip, pickle, pickletools
import sys
import pandas as pd


import pandas as pd
import numpy as np
import gzip, pickle, pickletools
import time
import cloudpickle as cp
import urllib.request
import joblib
sys.path.append('./')


class RecomendacionesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recomendaciones'

    basepath = "https://www.dropbox.com/s/"

    here = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(here)

    # Dataframe que contiene la información del material biblográfico
    material_path = os.path.join(here, 'model/TABLA_JOIN.json')
    lib_material = pd.read_json(basepath + "q38zr341seq7rkf/joinTablas.json?dl=1")
    sys.path.append(material_path)

    # Dataframe que contiene la información de las temáticas del material
    themes_path = os.path.join(here, 'model/Libros.json')
    lib_themes = pd.read_json(basepath + 'a2wops7yxdjd2ea/Libros.json?dl=1')
    sys.path.append(themes_path)

    # Dataframe que contiene la información de las recomendaciones
    lib_recommendations = pd.read_json(basepath + '1o0ygtyegofr6pw/recomedaciones_finales.json?dl=1')

    recommendation_predictor = " "
