from django.db import models

# Create your models here.

class Articulo(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()
    precio_unitario = models.FloatField(default=0)
    activo = models.BooleanField(default=True)