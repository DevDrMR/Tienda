from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.db import models
import os

# Create your models here.

# Modelo del Proveedor
class Proveedor(models.Model):
    rfc = models.CharField(max_length=13)
    razon_social = models.CharField(max_length=90)
    email = models.EmailField(max_length=90)
    fecha_alta = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.razon_social


# Modelo de los articulos
class Articulo(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()
    imagen  = models.ImageField(upload_to="productos", null=True, blank=True)
    precio_unitario = models.FloatField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

###################################################################################
# Para manejar la eliminación de las imagenes cuando se elimine un articulo de la #
# base de datos se recurre a signals, lo que permite que se eliminen las imágenes # 
# ya sea por el metodo de la clase o o de un queryset                             #
###################################################################################
@receiver(pre_delete, sender=Articulo)
def articulo_delete_handler(sender, instance, **kwargs):
    if os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)
    