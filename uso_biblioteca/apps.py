from django.apps import AppConfig
import pandas as pd
import sys
sys.path.append('../')
import Constants


class UsoBibliotecaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'uso_biblioteca'

    lib_material = pd.read_json(Constants.Constants.join)
    basepath = "https://www.dropbox.com/s/"
    lib_feedback= pd.DataFrame(pd.read_json(Constants.Constants.feedback))
    lib_pesos_usuarios= pd.DataFrame(pd.read_json(Constants.Constants.pesos_usuarios_unidad))
    lib_fake_user_info = pd.DataFrame(pd.read_json(basepath + 'vb2uehwpmn2sboz/MOCK_DATA_ESTUDIANTES.json?dl=1' ))
    lib_recomendaciones_completas= pd.DataFrame(pd.read_json(Constants.Constants.recomendaciones))
    lib_recomendaciones_finalesMasFeedback = pd.DataFrame(pd.read_json(Constants.Constants.recomendaciones))
