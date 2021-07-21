from django.contrib import admin
from django.urls import path

from . import views

app_name = "votante_app"
urlpatterns = [
    path('indexRaiz/', views.VerificarVotante.as_view(), name='verificacion-votante'),# se debe borrar el indexRaiz y dejar solo '' raiz
    path('eleccionCandidato/<cc>/', views.EleccionCandidato.as_view(), name='eleccion-votante'),
    path('error/', views.ErrorVotante.as_view(), name='error-votante'),
    path('agradecimiento/', views.agradecimientoVotante.as_view(), name='agradecimiento-votante'),
    path('reporte/', views.reporteVotacion.as_view(), name='reporte-votos'),
    path('tabla/', views.TablaVotantesView.as_view(), name='tabla-votos'),
    path('', views.IndexTemporal.as_view(), name='temporal-index'), # esta se debe quitar, al momento de votar

]
