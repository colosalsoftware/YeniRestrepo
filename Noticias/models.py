from django.db import models
from django.utils import timezone

class Comunicado(models.Model):
    imagen = models.ImageField(upload_to='comunicados/')
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True, editable=False)
    estado = models.BooleanField(default=False, verbose_name="¿Mostrar en sitio?")

    def __str__(self):
        return self.titulo