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
sys.path.append('../')
import Constants



class RecomendacionesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recomendaciones'

    basepath = 'www.dropbox.com/s/'

    # Dataframe que contiene la información del material
    lib_material = pd.read_json(Constants.Constants.join)

    # Dataframe que contiene la información de las recomendaciones
    lib_recommendations = pd.read_json(Constants.Constants.recomendaciones)

    recommendation_predictor = " "
