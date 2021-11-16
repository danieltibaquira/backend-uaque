from django.apps import AppConfig
import pandas as pd


class UsoBibliotecaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'uso_biblioteca'

    basepath = "https://www.dropbox.com/s/"
    lib_material = pd.read_json(basepath + "q38zr341seq7rkf/joinTablas.json?dl=1")
    lib_feedback= pd.DataFrame(pd.read_json(basepath + "fn2o86tbrplkjpd/recomedaciones_finalesMasFeedback.json?dl=1"))
    lib_pesos_usuarios= pd.DataFrame(pd.read_json(basepath + "voqnwdzt8cwyr7u/pesos_norm_id_unidad.json?dl=1"))
    lib_fake_user_info = pd.DataFrame(pd.read_json(basepath + 'vb2uehwpmn2sboz/MOCK_DATA_ESTUDIANTES.json?dl=1' ))
