from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('inicio/', cargar_inicio),
    path("libros/", cargar_vista_libros),
    path("libros/crear", crear_libro)
]