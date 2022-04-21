from django.db import models

# Create your models here.
class Editorial(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=150)




class Libro(models.Model):

    id = models.IntegerField(primary_key= True)
    nombre = models.TextField(max_length=150)
    num_paginas = models.IntegerField()
    fecha_publicacion = models.DateTimeField()
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, default=None)

