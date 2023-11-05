from django.shortcuts import render, get_object_or_404
from Mision_Animal.models import Animalito
from Negocios.models import Emprendimiento
from Agenda.models import Evento
from Noticias.models import Comunicado
# Create your views here.

def inicio(request):
    eventos=Evento.objects.all()
    context = {
        'eventos':eventos,
    }
    return render(request,'inicio/home.html',context)

def peluditos(request):
    peludos=Animalito.objects.filter(esta_disponible=True)
    context = {
        'peluditos':peludos,
    }
    return render(request,'peluditos/peludito.html',context)

def negocios(request):
    negocios=Emprendimiento.objects.filter(mostrar_en_el_sitio=True)
    context = {
        'negocios':negocios,
    }
    return render(request,'negocios/negocios.html',context)

def noticias_view(request, noticia_id=None):
    noticias = Comunicado.objects.filter(estado=True)
    noticia_seleccionada = None

    if noticia_id:
        noticia_seleccionada = Comunicado.objects.get(pk=noticia_id, estado=True)

    context = {
        'noticias': noticias,
        'noticia_seleccionada': noticia_seleccionada,
    }

    return render(request, 'noticias/noticias.html', context)
    