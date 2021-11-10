from django.apps import AppConfig
import pandas as pd


class PerfilGrupalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'perfil_grupal'

    basepath = "https://www.dropbox.com/s/"
    lib_material = pd.read_json(basepath + "q38zr341seq7rkf/joinTablas.json?dl=1")
    lib_feedback = pd.read_json(basepath + "0xczxjo927nsn0k/feedback_daniel.json?dl=1")
