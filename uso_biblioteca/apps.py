from django.apps import AppConfig
import pandas as pd


class UsoBibliotecaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'uso_biblioteca'

    basepath = "https://www.dropbox.com/s/"
    lib_material = pd.read_json(basepath + "q38zr341seq7rkf/joinTablas.json?dl=1")
