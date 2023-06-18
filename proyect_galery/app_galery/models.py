from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(null=False, max_length=50)
    descripcion = models.TextField(max_length=500)
    precio = models.DecimalField(max_digits=7, decimal_places=2)

