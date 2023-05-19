from django.shortcuts import render

def index(request):
    # Lógica de la vista
    return render(request, 'index.html')

def crear_turno(request):
    # Lógica para crear un turno
    return render(request, 'crear_turno.html')