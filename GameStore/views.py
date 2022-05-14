from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def cargar_inicio(request):

    videojuegos = Videojuego.objects.all()
    return render(request, "inicio.html", {"videojuegos":videojuegos})

def cargar_lista(request):

    videojuegos = Videojuego.objects.all()
    return render(request, "ListadoVideojuegos.html", {"videojuegos":videojuegos})

def cargar_listaN(request):

    videojuegos = Videojuego.objects.all()
    return render(request, "ListadoVideojuegosNintendo.html", {"videojuegos":videojuegos})

def cargar_listaS(request):

    videojuegos = Videojuego.objects.all()
    return render(request, "ListadoVideojuegosSony.html", {"videojuegos":videojuegos})

def cargar_listaX(request):

    videojuegos = Videojuego.objects.all()
    return render(request, "ListadoVideojuegosXbox.html", {"videojuegos":videojuegos})


def cargar_indice(request):

    videojuegos = Videojuego.objects.all()
    return render(request, "indice.html", {"videojuegos":videojuegos})


def registrarVideojuego(request):

    id = request.POST['numId']
    nombre = request.POST['txtNombre']
    num_horas = request.POST['numHoras']
    genero = request.POST['txtGenero']
    compania = request.POST['txtCompania']
    fecha_publicacion = request.POST['dateFecha']

    videojuego = Videojuego.objects.create(
        id=id, nombre=nombre, num_horas=num_horas, genero=genero, compania=compania, fecha_publicacion=fecha_publicacion
    )
    return redirect('/')

def edicionVideojuego(request, id):
    videojuego = Videojuego.objects.get(id=id)
    return render(request, "edicionVideojuego.html", {"videojuego":videojuego})


def editarVideojuego(request):
    id = request.POST['numId']
    nombre = request.POST['txtNombre']
    num_horas = request.POST['numHoras']
    genero = request.POST['txtGenero']
    compania = request.POST['txtCompania']
    fecha_publicacion = request.POST['dateFecha']

    videojuego = Videojuego.objects.get(id=id)
    videojuego.nombre = nombre
    videojuego.num_horas = num_horas
    videojuego.genero = genero
    videojuego.compania = compania
    videojuego.fecha_publicacion = fecha_publicacion
    videojuego.save()
    return redirect('/')




def eliminarVideojuego(request, id):
    videojuego = Videojuego.objects.get(id=id)
    videojuego.delete()
    return redirect('/')

