from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [

    path('', cargar_indice),
    path('editar/', cargar_inicio),
    path('listadovideojuegos/', cargar_lista),
    path('listadovideojuegosNintendo/', cargar_listaN),
    path('listadovideojuegosSony/', cargar_listaS),
    path('listadovideojuegosXbox/', cargar_listaX),
    path('registrarVideojuego/', registrarVideojuego),
    path('edicionVideojuego/<id>', edicionVideojuego),
    path('editarVideojuego/', editarVideojuego),
    path('eliminarVideojuego/<id>', eliminarVideojuego),


]