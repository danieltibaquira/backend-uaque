from django.urls import path, include
from .views import (
    DashboardControlPanelMaterialUpdate,
    DashboardControlPanelPrestamosUpdate,
    DashboardFeedbackIndividual,
    DashboardFeedbackIndividualUtilsOption,
    DashboardFeedbackPorDewey,
    DashboardFeedbackPorDeweyUtilsOption,
    DashboardFeedbackUtilsDeweyList,
    DashboardGrupos,
    DashboardGruposUtilsDeweyList,
    DashboardPertenencia,
    DashboardPertenenciaUtilsUpdateBookList,
    DashboardPertenenciaUtilsUpdateOptions,
)
from .views import LibUseAPIView
from .views import AzUseAPIView
from .views import RepoUseAPIView
from .views import LibResAPIView
from .views import AzResAPIView
from .views import RepoResAPIView
from .views import DashboardFeedback
from .views import DataPrepAPIView

# URL Base para el servicio
baseURL = "suj-e-004"

urlpatterns = [
    # URLs registradas para el servicio
    path("suj-e-004/libUse", LibUseAPIView.as_view()),
    path("suj-e-004/azUse", AzUseAPIView.as_view()),
    path("suj-e-004/repoUse", RepoUseAPIView.as_view()),
    path("suj-e-004/libRes", LibResAPIView.as_view()),
    path("suj-e-004/azRes", AzResAPIView.as_view()),
    path("suj-e-004/repoRes", RepoResAPIView.as_view()),
    path("suj-e-004/dataprep", DataPrepAPIView.as_view()),
    path("suj-e-004/DashboardFeedback", DashboardFeedback.as_view()),
    path(
        "suj-e-004/DashboardFeedbackUtilsDeweyList",
        DashboardFeedbackUtilsDeweyList.as_view(),
    ),
    path("suj-e-004/DashboardGrupos", DashboardGrupos.as_view()),
    path(
        "suj-e-004/DashboardGruposUtilsDeweyList",
        DashboardGruposUtilsDeweyList.as_view(),
    ),
    path("suj-e-004/DashboardPertenencia", DashboardPertenencia.as_view()),
    path(
        "suj-e-004/DashboardFeedbackUtilsDeweyList",
        DashboardFeedbackUtilsDeweyList.as_view(),
    ),
    path(
        "suj-e-004/DashboardPertenencia",
        DashboardPertenencia.as_view(),
    ),
    path(
        "suj-e-004/DashboardPertenenciaUtilsUpdateBookList",
        DashboardPertenenciaUtilsUpdateBookList.as_view(),
    ),
    path(
        "suj-e-004/DashboardPertenenciaUtilsUpdateOptions",
        DashboardPertenenciaUtilsUpdateOptions.as_view(),
    ),
    path(
        "suj-e-004/DashboardFeedbackPorDewey",
        DashboardFeedbackPorDewey.as_view(),
    ),
    path(
        "suj-e-004/DashboardFeedbackPorDeweyUtilsOption",
        DashboardFeedbackPorDeweyUtilsOption.as_view(),
    ),
    path(
        "suj-e-004/DashboardFeedbackIndividual",
        DashboardFeedbackIndividual.as_view(),
    ),
    path(
        "suj-e-004/DashboardFeedbackIndividualUtilsOption",
        DashboardFeedbackIndividualUtilsOption.as_view(),
    ),
    path(
        "suj-e-004/DashboardControlPanelMaterialUpdate",
        DashboardControlPanelMaterialUpdate.as_view(),
    ),
    path(
        "suj-e-004/DashboardControlPanelPrestamosUpdate",
        DashboardControlPanelPrestamosUpdate.as_view(),
    ),
]
