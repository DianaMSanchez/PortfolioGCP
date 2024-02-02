from django.shortcuts import render
from .forms import ContactoForms

# Create your views here.

def contacto(request):
    data = {
        'form' : ContactoForms
    } 

    if request.method == "POST":
        formulario = ContactoForms(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Guardado"
        else:
            data["form"] = formulario
    return render(request, "contacto.html", data)

