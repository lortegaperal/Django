from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [

    path('indice/', cargar_indice),
    path('', cargar_inicio),
    path('listadovideojuegos/', cargar_lista),
    path('registrarVideojuego/', registrarVideojuego),
    path('edicionVideojuego/<id>', edicionVideojuego),
    path('editarVideojuego/', editarVideojuego),
    path('eliminarVideojuego/<id>', eliminarVideojuego),


]