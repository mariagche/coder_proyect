from django import forms


class CursoFormulario(forms.Form):
    Nombre = forms.CharField(max_length=64)
    Comision = forms.IntegerField()
    Fecha_de_inicio = forms.IntegerField() 
       
class ProfesorFormulario(forms.Form):
    Nombre = forms.CharField(max_length=64)
    Apellido = forms.CharField(max_length=64)
    Comision = forms.IntegerField()
    Tema = forms.CharField(max_length=1000)
    fecha_de_nacimiento = forms.DateField() 
    profesion = forms.CharField(max_length=1000) 
    bio = forms.CharField(max_length=1000)
    curso = forms.IntegerField()
    dni = forms.CharField() 
    email = forms.EmailField() 

class EstudianteFormulario(forms.Form):
    Nombre = forms.CharField(max_length=64)
    Apellido = forms.CharField(max_length=64)
    Comision = forms.IntegerField()
    Tema = forms.CharField(max_length=2000)
    DNI = forms.CharField()
    fecha_de_nacimiento = forms.DateField()