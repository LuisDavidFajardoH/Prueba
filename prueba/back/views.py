from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'taller/listar_usuarios.html', {'usuarios': usuarios})


def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Guardar el usuario en la base de datos
            return redirect('back:listar_usuarios')
    else:
        form = UsuarioForm()
    
    return render(request, 'taller/crear_usuario.html', {'form': form})


def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect('back:listar_usuarios')


def pagina_inicio(request):
    return render(request, 'taller/index.html')

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)

    if request.method == 'POST':
        # Obtener los datos del formulario
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        numero_celular = request.POST.get('numero_celular')
        es_staff = request.POST.get('es_staff') == 'on'
        foto = request.FILES.get('foto')

        # Actualizar los valores del usuario
        usuario.nombres = nombres
        usuario.apellidos = apellidos
        usuario.numero_celular = numero_celular
        usuario.es_staff = es_staff
        if foto:
            usuario.foto = foto

        # Guardar los cambios en la base de datos
        usuario.save()

        return redirect('back:listar_usuarios')
    else:
        return render(request, 'taller/editar_usuario.html', {'usuario': usuario})