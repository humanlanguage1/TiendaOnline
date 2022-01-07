from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
      nombre = models.CharField(max_length=200)
      pub_date= models.DateTimeField(auto_now_add=True)
      def __str__(self):
            return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField("'fecha registro")
    imagen = models.ImageField(upload_to='productos', blank=True, null=True)
    
    def __str__(self):
            return self.nombre

class Cliente(models.Model):
      user = models.OneToOneField(User,on_delete=models.RESTRICT)
      doc_ide= models.CharField(max_length=200,blank=True)
      direccion = models.CharField(max_length=200,blank=True)
      telefono = models.CharField(max_length=20,blank=True)

      def __str__(self):
            return self.usuario.username