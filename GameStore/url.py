from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    path('', cargar_inicio),
    path('registrarVideojuego/', registrarVideojuego),
    path('eliminarVideojuego/<id>', eliminarCurso)

]