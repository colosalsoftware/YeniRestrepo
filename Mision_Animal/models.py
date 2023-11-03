from django.db import models

# Create your models here.
class Animalito(models.Model):
    foto = models.ImageField(upload_to='photos/Animalitos')
    nombre = models.CharField(max_length=200)
    edad = models.CharField(max_length=200)
    raza = models.CharField(max_length=200)
    tamaño = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=400)
    esta_disponible = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Animalito'
        verbose_name_plural = 'Animalitos'

    def __str__(self):
        return self.nombre