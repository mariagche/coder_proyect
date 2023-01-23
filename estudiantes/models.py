from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=64)
    comision = models.IntegerField()
    fecha_de_inicio = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombre}, {self.comision}, {self.fecha_de_inicio}"


class Estudiante(models.Model):
    Nombre = models.CharField(max_length=256)
    Apellido = models.CharField(max_length=256)
    DNI = models.CharField(max_length=32)
    email = models.EmailField()
    Fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.Apellido}, {self.Nombre}, {self.DNI},{self.email}, {self.Fecha_nacimiento}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    profesion = models.CharField(max_length=128)
    bio = models.TextField(null=True)
    comision = models.IntegerField()     #(required=True, max_value=2000)
    tema = models.CharField(max_length=32)
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.dni}, {self.email}, {self.fecha_nacimiento}, {self.profesion},{self.bio},{self.comision},{self.tema}"


#class Entregable(models.Model):
    #nombre = models.CharField(max_length=256)
   # fecha_entrega = models.DateTimeField()
   # esta_aprobado = models.BooleanField(default=False)


#class Instituto(models.Model):
    #nombre = models.CharField(max_length=256)
