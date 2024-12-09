from django.db import models # type: ignore

# Create your models here.
class Genero(models.Model):
    #Género musical.
    id = models.IntegerField(default=0, primary_key=True)
    nombre = models.CharField(max_length=25)
    origen = models.CharField(max_length = 400, null = True)

    def __str__(self):
        return self.nombre

class Artista(models.Model):
    #Artista que compone canciones.
    nombre = models.CharField(max_length=25)
    id = models.IntegerField(default=0,primary_key=True)
    fechaNacimiento = models.DateField(null = True)
    genero = models.ForeignKey(Genero, related_name="artistas", on_delete=models.CASCADE)
    imagen_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    #Canción perteneciente a un artista.
    nombre = models.CharField(max_length=25)
    fechaLanzamiento = models.DateField()
    artista = models.ForeignKey(Artista, related_name="canciones", on_delete=models.CASCADE)
    imagen_url = models.URLField(blank=True, null=True) #<img src = "{{cancion.img_url}}" alt = "Imagen">

    def __str__(self):
        return self.nombre 


