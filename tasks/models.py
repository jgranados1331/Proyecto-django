from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

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
    precio=models.IntegerField()
    Imagen=models.ImageField(upload_to='vehiculos', null=False)
    Descripcion=models.CharField(max_length=1000, null=False)
    slug=AutoSlugField(populate_from='nombre')

    def __str__(self):
        return self.nombre +'-'+ self.categoria.nombre
    
class Profile(models.Model):
    Imagen=models.ImageField(upload_to='users-profile', null=False)
    nombre=models.CharField(max_length=30, null=False)
    apellido=models.CharField(max_length=30, null=False)
    fecha_nacimiento=models.DateField(null=False)
    edad=models.CharField(max_length=2,null=False)
    celular=models.IntegerField(null=False)
    cc_passport=models.IntegerField(null=False)
    pais=models.CharField(max_length=30,null=False)
    ciudad=models.CharField(max_length=30,null=False)
    domicilio=models.CharField(max_length=50,null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre + '-' + self.user.username
    
class Order(models.Model):
    ordernum=models.CharField(max_length=9,null=True,blank=True)
    customer=models.CharField(max_length=200,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.ordernum
    
class OrderDetail(models.Model):
    product=models.ForeignKey(Vehiculo,on_delete=models.CASCADE)
    cant=models.IntegerField(default=1)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product.nombre
    
    
