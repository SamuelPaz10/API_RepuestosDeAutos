
# Create your models here.
from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)

class Auto(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

class Vendedor(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion    

class Modelo(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

class Cliente(models.Model):
    id_nacional = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField()
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " " + self.apellido
    
    class Repuesto(models.Model):
        nombre = models.CharField(max_length=200)
        descripcion = models.CharField(max_length=200)
    anio = models.DateField()
    id_origen= models.CharField(max_length=200)
    id_modelo = models.CharField(max_length=200)
    precio = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    
class RepuestoModelos(models.Model):
    id_repuesto = models.ForeignKey(Repuesto, on_delete=models.CASCADE)
    id_modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_repuesto.nombre + " " + self.id_modelo.descripcion

class Genero(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion