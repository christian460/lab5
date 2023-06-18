from django.db import models

# Create your models here.
class Pictures_product(models.Model):
    nombre = models.CharField(max_length=50, null = False)
    description = models.TextField(max_length=500)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.ImageField(upload_to="imagenes", null = True)
