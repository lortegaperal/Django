from django.db import models
from django_enumfield import enum
from django_enumfield.db.fields import EnumField


class Videojuego(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=150)
    num_horas = models.IntegerField()
    genero = models.TextField(max_length=150)
    fecha_publicacion = models.DateField()
    compania = EnumField("Nintendo", "Sony", "Xbox")


    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.id)


