from django.db import models

# Create your models here.
class Genero(models.Model):
    #Género musical.
    nombre = models.CharField(25)

    def __str__(self):
        return self.nombre

class Artista(models.Model):
    #Artista que compone canciones.
    nombre = models.CharField(25)
    id = models.PositiveIntegerFieldIntegerField()
    genero = models.ForeignKey(Genero, related_name="genero", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    #Canción perteneciente a un artista.
    nombre = models.CharField(25)
    fechaLanzamiento = models.DateField()
    artista = models.ForeignKey(Artista, related_name="autor", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ". Por: " + self.__str__(self.artista)
