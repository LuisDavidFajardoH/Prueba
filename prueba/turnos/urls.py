from django.urls import path
from . import views
from django.shortcuts import render, get_object_or_404, redirect
from .models import Turno
from .forms import TurnoForm

# Resto del código de las vistas...


app_name = 'turnos'

urlpatterns = [
    path('', views.index, name='index'), 
    path('listar_turnos/', views.listar_turnos, name='listar_turnos'),
    path('crear_turno/', views.crear_turno, name='crear_turno'),
    path('editar_turno/<int:id>/', views.editar_turno, name='editar_turno'),
    path('eliminar_turno/<int:id>/', views.eliminar_turno, name='eliminar_turno'),
]
