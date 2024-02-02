from django.http import HttpResponse
from django.template import Template, Context
import datetime


def presentacion(request): #Presentación 
    return render(request, 'presentacion.html')
    #documento = open("C:/Proyectos Django/PortfolioGCP/PortfolioGCP/template/presentacion.html")
    #date = Template(documento.read())
    #documento.close()
    #ctx = Context()
    #documento_Renderizado = date.render(ctx)
    #return HttpResponse(documento_Renderizado)

def proyecto(request): #Proyecto 

    return HttpResponse("Aquí van los proyectos")

def estudios(request): #Estudios 

    return HttpResponse("Estudios")

def publicaciones(request): #Publicaciones 

    return HttpResponse("Publicaciones")

def redes_sociales(request): #Redes sociales 

    return HttpResponse("Redes sociales")

                        


