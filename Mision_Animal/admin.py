from django.contrib import admin
from .models import Animalito

# Register your models here.

class AnimalitoAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad','raza','tamaño','descripcion','esta_disponible')
    list_display_links = ('nombre',)
admin.site.register(Animalito,AnimalitoAdmin)
# Register your models here.
