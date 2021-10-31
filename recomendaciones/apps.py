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

    material_path = os.path.join(here, 'model/TABLA_JOIN.json')
    # lib_material = pd.read_json(material_path)
    lib_material = pd.read_json(basepath + "q38zr341seq7rkf/joinTablas.json?dl=1")
    sys.path.append(material_path)

    themes_path = os.path.join(here, 'model/Libros.json')
    # lib_themes = pd.read_json(themes_path)
    lib_themes = pd.read_json(basepath + 'a2wops7yxdjd2ea/Libros.json?dl=1')
    sys.path.append(themes_path)

    lib_recommendations = pd.read_json(basepath + '1o0ygtyegofr6pw/recomedaciones_finales.json?dl=1')

    recommendation_predictor = " "

    ''' SAR RECOMMENDER
    lib_group_pert = pd.read_json(basepath + 'zuwne8aii9dknvs/pesos_clustering_unidad.json?dl=1')

    sar_model_path = basepath + '2dljfcxbtwuvh1w/sar_trained_model_du_full.pkl?dl=1'
    with gzip.open(urllib.request.urlopen(sar_model_path), 'rb') as f:
        p = pickle.Unpickler(f)
        sar_predictor = p.load()

    predictor = sar_predictor
    '''
