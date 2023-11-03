from django.db import models

# Create your models here.
class Emprendimiento(models.Model):
    Logo = models.ImageField(upload_to='photos/Emprendimientos')
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=400)
    pagina_web = models.URLField(max_length=400)
    mostrar_en_el_sitio = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Emprendimiento'
        verbose_name_plural = 'Emprendimientos'

    def __str__(self):
        return self.nombre