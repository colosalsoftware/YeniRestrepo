from django.contrib import admin
from django import forms
from .models import Evento

# Register your models here.
class EventoForm(forms.ModelForm):
    fecha = forms.SplitDateTimeField(widget=admin.widgets.AdminSplitDateTime())
    class Meta:
        model = Evento
        fields = '__all__'

class EventoAdmin(admin.ModelAdmin):
    form = EventoForm
    list_display = ('fecha', 'nombre_del_evento', 'descripcion', 'lugar')

admin.site.register(Evento, EventoAdmin)