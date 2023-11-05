from django.db import models

# Create your models here.
class Evento(models.Model):
    fecha = models.DateTimeField()
    nombre_del_evento = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=500, blank=True)
    lugar = models.CharField(max_length=500)
    link_maps = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    def __str__(self):
        return str(self.nombre_del_evento)