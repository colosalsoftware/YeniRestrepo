from django.contrib import admin
from .models import Emprendimiento

# Register your models here.
class EmprendimientoAdmin(admin.ModelAdmin):
    list_display = ('nombre','pagina_web','mostrar_en_el_sitio')
    list_display_links = ('nombre',)
admin.site.register(Emprendimiento,EmprendimientoAdmin)