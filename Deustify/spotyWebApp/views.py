from django.shortcuts import render
from .models import Genero, Artista, Cancion
# Create your views here.


from django.http import HttpResponse,HttpResponseNotFound
def index(request):
    return HttpResponse("Hello, world!")

def listaGeneros(request):
    generos = Genero.objects.order_by('nombre')
    nombre_generos = ', '.join([genero.nombre for genero in generos])
    return HttpResponse(nombre_generos)

def detalleGeneros(request, id_genero):
    try:
        genero = Genero.objects.get(pk=id_genero)
        artistas = genero.genero.all()

        cadenaDeTexto = f"{genero.nombre} - ID: {genero.id}\n"

        if artistas.exists():
            cadenaDeTexto += "Artistas:\n"
            for artista in artistas:
                cadenaDeTexto += f"- {artista.id}: {artista.nombre}.\n"
        else:
            cadenaDeTexto += "No hay artistas en este género."

        return HttpResponse(cadenaDeTexto)
    except artista.DoesNotExist:
        return HttpResponseNotFound("Genero no encontrado")

def listaArtistas(request):
    artistas = Artista.objects.order_by('nombre')
    nombre_artistas = ', '.join([artista.nombre for artista in artistas])
    return HttpResponse(nombre_artistas)

def detalleArtistas(request, id_artista):
    try:
        artista = Artista.objects.get(pk=id_artista)
        canciones = artista.autor.all()

        cadenaDeTexto = f"{artista.nombre} - ID: {artista.id}\n"

        if canciones.exists():
            cadenaDeTexto += "Canciones:\n"
            for cancion in canciones:
                cadenaDeTexto += f"- {cancion.nombre}, fecha de lanzamiento: {cancion.fechaLanzamiento}.\n"
        else:
            cadenaDeTexto += "No hay canciones creadas por este artista."

        return HttpResponse(cadenaDeTexto)
    except artista.DoesNotExist:
        return HttpResponseNotFound("Artista no encontrado")

def listaCanciones(request):
    canciones = Genero.objects.order_by('fechaLanzamiento')
    nombre_canciones = ', '.join([Cancion.nombre for cancion in canciones])
    return HttpResponse(nombre_canciones)