import dropbox


class Constants:
    basepath = "https://www.dropbox.com/s/"

    lib_material_pre = basepath + "upzlpsf0a7en5el/material_original.json?dl=1"
    lib_material_pre_name = "/material_original.json"

    lib_prestamos_pre = basepath + "oq9pnbhcsuq50by/prestamos_original.json?dl=1"
    lib_prestamos_pre_name = "/prestamos_original.json"

    join = basepath + "5lkfj8k5yji3mdo/join.json?dl=1"
    join_name = "/join.json"

    feedback = basepath + "gk705nycjc5hza0/feedback_users.json?dl=1"
    feedback_name = "/feedback_users.json"

    pesos_clust_unidad = basepath + "l7u8789vfvpg2lu/pesos_clustering_unidad.json?dl=1"
    pesos_clust_unidad_name = "/pesos_clustering_unidad.json"

    pesos_clust_decena = basepath + "athucpuhenn1km8/pesos_clustering_decena.json?dl=1"
    pesos_clust_decena_name = "/pesos_clustering_decena.json"

    pesos_clust_centena = (
        basepath + "xgubsempv4z6wwx/pesos_clustering_centena.json?dl=1"
    )
    pesos_clust_centena_name = "/pesos_clustering_centena.json"

    pesos_usuarios_unidad = (
        basepath + "cef65a12jcyoezm/pesos_usuario_x_dewey_unidad.json?dl=1"
    )
    pesos_usuarios_unidad_name = "/pesos_usuario_x_dewey_unidad.json"

    pesos_usuarios_decena = (
        basepath + "ieis4vsxyct0hyc/pesos_usuario_x_dewey_decena.json?dl=1"
    )
    pesos_usuarios_decena_name = "/pesos_usuario_x_dewey_decena.json"

    pesos_usuarios_centena = (
        basepath + "6tpbup9wnmcjy34/pesos_usuario_x_dewey_centena.json?dl=1"
    )
    pesos_usuarios_centena_name = "/pesos_usuario_x_dewey_centena.json"

    recomendaciones = basepath + "no9kiho5ym8jvyr/recomendaciones.json?dl=1"
    recomendaciones_name = "/recomendaciones.json"

    # recomendaciones_finalesMasFeedback = basepath + "ii7tj2jkmpt2fi9/recomedaciones_feedback.json?dl=1"
    # recomendaciones_finalesMasFeedback_name = "/recomendaciones_finalesMasFeedback.json"

    lib_material_post = basepath + "ebhbn5nfadoc36s/material_limpio.json?dl=1"
    lib_material_post_name = "/material_limpio.json"

    lib_prestamos_post = basepath + "wk4wj1b8lex6uas/prestamos_limpios.json?dl=1"
    lib_prestamos_post_name = "/prestamos_limpios.json"
    # Código de acceso para el API de dropbox
    TOKEN = "WEHCPUrHMvEAAAAAAAAAAQax8AS74zZTuv3eDQCuAJbcHMPbH5M0SdPa0tyJ9X2m"

    # Inicialización del objeto Dropbox
    dbx = dropbox.Dropbox(TOKEN)

    def __init__():
        return
