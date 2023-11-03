from django.shortcuts import render, get_object_or_404
from Mision_Animal.models import Animalito
from Negocios.models import Emprendimiento
# Create your views here.

def inicio(request):
    return render(request,'home.html')