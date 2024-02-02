from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.
class Proyecto(models.Model):
    nombre = CharField(max_length=100)
    descripcion = CharField(max_length=500)
    url = URLField (blank = True)
    image = ImageField(upload_to='portafolio/images/')