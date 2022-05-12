from django.db import models

class Consola(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=150)
    generacion = models.TextField(max_length=150)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre,self.id)



class Compania(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=150)
    independiente = models.BooleanField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre,self.id)


class Videojuego(models.Model):
    id = models.IntegerField(primary_key= True)
    nombre = models.TextField(max_length=150)
    num_horas = models.IntegerField()
    genero = models.TextField(max_length=150)
    fecha_publicacion = models.DateField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre,self.id)


