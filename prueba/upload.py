import os
import django

#Archivo que use para hacer pruebas de subida

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prueba.settings")
django.setup()


from django.core.files import File
from back.models import Usuario

# Ruta de la imagen que quieres subir
ruta_imagen = r'C:\Users\luisd\Downloads\descargar.jpg'



# Crea una instancia de Usuario
usuario = Usuario(
    nombres='Felipe',
    apellidos='Herrera',
    numero_celular='2003148',
    numero_identificacion='124124',
    es_staff=False,
)

# Abre la imagen en modo binario
with open(ruta_imagen, 'rb') as f:
    # Crea un objeto File a partir del archivo
    imagen = File(f)

    # Asigna la imagen al campo 'foto' del usuario
    usuario.foto.save('descargar.jpg', imagen, save=True)

# Guarda el usuario en la base de datos
usuario.save()
