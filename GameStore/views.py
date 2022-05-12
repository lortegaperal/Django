from django.shortcuts import render
from .models import *



# Create your views here.
def cargar_inicio(request):

    consola = Consola.objects.all()
    compania = Compania.objects.all()
    videojuegos = Videojuego.objects.all()

    return render(request, "inicio.html", {"videojuegos":videojuegos})



