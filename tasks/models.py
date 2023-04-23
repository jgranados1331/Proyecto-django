from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Taks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '- by' + self.user.username

class Categoria(models.Model):
    nombre=models.CharField(max_length=10, unique=True, null=False)
    

    def __str__(self):
        return self.nombre


class subcategoria(models.Model):
    Nombre=models.CharField(max_length=20, null=False)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre +  '-by-'  +  self.categoria.nombre

class Marca(models.Model):
    nombre=models.CharField(max_length=30, unique=True, null=False)
    

    def __str__(self):
        return self.nombre
    
class Vehiculo(models.Model):
    nombre=models.CharField(max_length=30, unique=True, null=False)
    marca=models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria=models.ForeignKey(subcategoria, on_delete=models.CASCADE)
    caballos=models.CharField(max_length=15)
    motor=models.CharField(max_length=40)
    precio=models.CharField(max_length=15)
    Imagen=models.ImageField(upload_to='vehiculos', null=False)
    Descripcion=models.CharField(max_length=1000, null=False)

    def __str__(self):
        return self.nombre +'-'+ self.categoria.nombre