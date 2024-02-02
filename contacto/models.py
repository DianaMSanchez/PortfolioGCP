from django.db import models
import datetime

# Create your models here.
opciones_consultas = [
    [0, "consulta"],
    [1, "sugerencia"],
    [2, "enhorabuena"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices= opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    date = models.DateField(datetime.date.today)

    def __str__(self):
        return self.nombre

