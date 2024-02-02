from django import forms
from .models import Proyecto

class ProyectoForms(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'url', 'image']
        #fields = '__all__'