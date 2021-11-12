from django.apps import AppConfig
import pandas as pd
import dropbox

class PerfilGrupalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'perfil_grupal'

    TOKEN = "WEHCPUrHMvEAAAAAAAAAAQax8AS74zZTuv3eDQCuAJbcHMPbH5M0SdPa0tyJ9X2m"

    dbx = dropbox.Dropbox(TOKEN)

    basepath = "https://www.dropbox.com/s/"
    lib_material = pd.read_json(basepath + "q38zr341seq7rkf/joinTablas.json?dl=1")
    lib_feedback = pd.read_json(basepath + "gk705nycjc5hza0/feedback_users.json?dl=1")
