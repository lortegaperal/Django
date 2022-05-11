from django.shortcuts import render
from .models import *



# Create your views here.
def cargar_inicio(request):
    return render(request, "inicio.html")

def cargar_vista_libros(request):
    lista_libros = Libro.objects.all()
    return render(request, "libros.html", {"libros": lista_libros})

def crear_libro(request):
    return None