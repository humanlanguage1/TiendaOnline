from django.shortcuts import render
from django.db import models

# Create your views here.
#def index(request):
  #  lista_productos = Producto.objec 
class Categoria(models.Model):
      nombre = models.CharField(max_length=200)
      pub_date= models.DateTimeField(auto_now_add=True)
      def __str__(self):
            return self.nombre

class Product(models.Model):
    category = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField("'fcha registro")
    imagen = models.ImageField(upload_to='productos', blank=True, null=True)
    
    def __str__(self):
            return self.nombre