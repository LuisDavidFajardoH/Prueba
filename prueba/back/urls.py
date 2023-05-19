from django.urls import path
from . import views

app_name = 'back'

urlpatterns = [
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('', views.pagina_inicio, name='pagina_inicio'),
]

