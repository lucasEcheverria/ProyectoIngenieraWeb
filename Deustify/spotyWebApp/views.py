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

def listaArtistas(request):
    artistas = Artista.objects.order_by('nombre')
    nombre_artistas = ', '.join([artista.nombre for artista in artistas])
    return HttpResponse(nombre_artistas)

def listaCanciones(request):
    canciones = Genero.objects.order_by('fechaLanzamiento')
    nombre_canciones = ', '.join([Cancion.nombre for cancion in canciones])
    return HttpResponse(nombre_generos)