from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Turno
from .forms import TurnoForm
from back.models import Usuario


class IndexView(generic.View):
    def get(self, request):
        form = TurnoForm()
        usuarios = Usuario.objects.all()
        context = {
            'usuarios': usuarios,
            'form': form
        }
        return render(request, 'prueba/index.html', context)

    def post(self, request):
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnos:listar_turnos')

        usuarios = Usuario.objects.all()
        context = {
            'usuarios': usuarios,
            'form': form
        }
        return render(request, 'prueba/index.html', context)


class ListarTurnosView(generic.ListView):
    model = Turno
    template_name = 'turnos/listar_turnos.html'
    context_object_name = 'turnos'


class CrearTurnoView(generic.CreateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'turnos/crear_turno.html'
    success_url = reverse_lazy('turnos:listar_turnos')

    def form_valid(self, form):
        messages.success(self.request, '¡El turno se ha creado correctamente!')
        return super().form_valid(form)


class EditarTurnoView(generic.UpdateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'turnos/editar_turno.html'
    success_url = reverse_lazy('turnos:listar_turnos')


class EliminarTurnoView(generic.DeleteView):
    model = Turno
    template_name = 'turnos/eliminar_turno.html'
    success_url = reverse_lazy('turnos:listar_turnos')


class DetalleTurnoView(generic.DetailView):
    model = Turno
    template_name = 'turnos/detalle_turno.html'
    context_object_name = 'turno'
