from django.urls import path
from . import views

app_name = 'turnos'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('listar/', views.ListarTurnosView.as_view(), name='listar_turnos'),
    path('crear/', views.CrearTurnoView.as_view(), name='crear_turno'),
    path('editar/<int:pk>/', views.EditarTurnoView.as_view(), name='editar_turno'),
    path('eliminar/<int:pk>/', views.EliminarTurnoView.as_view(), name='eliminar_turno'),
    path('detalle/<int:pk>/', views.DetalleTurnoView.as_view(), name='detalle_turno'),
]
