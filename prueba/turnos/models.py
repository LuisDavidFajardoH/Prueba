from django.db import models
from django.contrib.auth.models import User



class Usuario(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    numero_celular = models.CharField(max_length=20)
    numero_identificacion = models.CharField(max_length=20)
    es_staff = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='fotos', default='fotos/descargar.jpg')

    def __str__(self):
        return self.nombres + ' ' + self.apellidos


class Turno(models.Model):
    numero_turno = models.CharField(max_length=10)
    hora_creacion_turno = models.DateTimeField(auto_now_add=True)
    ESTADOS_TURNO = [
        ('Pendiente', 'Pendiente'),
        ('Activo', 'Activo'),
        ('Finalizado', 'Finalizado'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS_TURNO, default='Pendiente')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    usuario_staff = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='turnos_staff', null=True, blank=True)

    def __str__(self):
        return self.numero_turno
    

