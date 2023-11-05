from django.contrib import admin
from .models import Comunicado
from django.utils.html import format_html


class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'estado')
    def estado_custom(self, obj):
        if obj.estado:
            return format_html('<img src="https://static-files-concejo-caldas.s3.amazonaws.com/static/admin/img/icon-yes.svg" width="16" height="16" />')
        else:
            return format_html('<img src="https://static-files-concejo-caldas.s3.amazonaws.com/static/admin/img/icon-no.svg" width="16" height="16" />')

admin.site.register(Comunicado, ComunicadoAdmin)

