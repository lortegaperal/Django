# Generated by Django 4.0.3 on 2022-05-12 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GameStore', '0003_compania_consola_videojuego_remove_libro_editorial_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videojuego',
            name='fecha_publicacion',
        ),
    ]
