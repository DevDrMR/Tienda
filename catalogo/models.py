from django.db import models

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
    nombre = models.CharField(max_length=45, help_text="Aquí usted va a escribir el nombre del proyecto")
    descripcion = models.TextField()
    imagen  = models.ImageField(upload_to="productos", null=True, blank=True)
    precio_unitario = models.FloatField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre