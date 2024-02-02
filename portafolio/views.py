from django.shortcuts import render
from .models import Proyecto
from .forms import ProyectoForms

# Create your views here.
def presentacion(request): #Presentación 
    projects = Proyecto.objects.all
    return render(request, 'presentacion.html', {'projects' : projects})

def proyectosAdd (request) : #Add Proyectos 
    data = {
        'formProyecto' : ProyectoForms
    } 

    if request.method == "POST":
        formulario = ProyectoForms(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Proyecto Guardado"
        else:
            data["form"] = formulario
    return render(request, 'formularioProyectos.html', data)