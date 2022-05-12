from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    path('', cargar_inicio),
    path('registrarVideojuego/', registrarVideojuego),
    path('edicionVideojuego/<id>', edicionVideojuego),
    path('editarVideojuego/', editarVideojuego),
    path('eliminarVideojuego/<id>', eliminarVideojuego),


]