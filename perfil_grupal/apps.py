from django.apps import AppConfig
import pandas as pd
import dropbox

class PerfilGrupalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'perfil_grupal'

    # Código de acceso para el API de dropbox
    TOKEN = "WEHCPUrHMvEAAAAAAAAAAQax8AS74zZTuv3eDQCuAJbcHMPbH5M0SdPa0tyJ9X2m"

    # Inicialización del objeto Dropbox
    dbx = dropbox.Dropbox(TOKEN)

    basepath = "https://www.dropbox.com/s/"

    # Dataframe que contiene la información del material biblográfico
    lib_material = pd.read_json(basepath + "q38zr341seq7rkf/joinTablas.json?dl=1")

    # Dataframe que contiene la información del feedback de los usuarios
    lib_feedback = pd.read_json(basepath + "gk705nycjc5hza0/feedback_users.json?dl=1")

    # Dataframe que contiene la información de las recomendaciones
    lib_recommendations = pd.read_json(basepath + '1o0ygtyegofr6pw/recomedaciones_finales.json?dl=1')
