from django.shortcuts import render, get_object_or_404, redirect
from .models import Turno
from .forms import TurnoForm
from back.models import Usuario

def index(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnos:listar_turnos')
    else:
        form = TurnoForm()

    usuarios = Usuario.objects.all()
    print(usuarios) 
    context = {
        'usuarios': usuarios,
        'form': form
    }

    return render(request, 'prueba/index.html', context)


def listar_turnos(request):
    turnos = Turno.objects.all()
    return render(request, 'turnos/listar_turnos.html', {'turnos': turnos})

def crear_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnos:listar_turnos')
    else:
        form = TurnoForm()
    return render(request, 'turnos/crear_turno.html', {'form': form})

def editar_turno(request, id):
    turno = get_object_or_404(Turno, id=id)
    if request.method == 'POST':
        form = TurnoForm(request.POST, instance=turno)
        if form.is_valid():
            form.save()
            return redirect('turnos:listar_turnos')
    else:
        form = TurnoForm(instance=turno)
    return render(request, 'turnos/editar_turno.html', {'form': form, 'turno': turno})

def eliminar_turno(request, id):
    turno = get_object_or_404(Turno, id=id)
    if request.method == 'POST':
        turno.delete()
        return redirect('turnos:listar_turnos')
    return render(request, 'turnos/eliminar_turno.html', {'turno': turno})
