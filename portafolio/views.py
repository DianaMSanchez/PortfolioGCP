from django.shortcuts import render
from .models import Proyecto

# Create your views here.
def presentacion(request): #Presentación 
    projects = Proyecto.objects.all
    return render(request, 'presentacion.html', {'projects' : projects})
