from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Genero, Artista, Cancion
# Create your views here.


from django.http import HttpResponse,HttpResponseNotFound
def index(request):
    return HttpResponse("Hello, world!")

def listaGeneros(request):
    generos = Genero.objects.order_by('nombre')
    contexto = {'generos' : generos}
    return render(request, 'listaGenero.html', contexto)

def detalleGeneros(request, id_genero):
    genero = get_object_or_404(Genero, pk=id_genero)
    contexto = {'genero': genero}
    return render(request, 'detalleGenero.html', contexto)

def listaArtistas(request):
    artistas = Artista.objects.order_by('nombre')
    nombre_artistas = ', '.join([artista.nombre for artista in artistas])
    return HttpResponse(nombre_artistas)

def detalleArtistas(request, id_artista):
    artista = get_object_or_404(Artista,pk=id_artista)
    contexto = {'artista':artista}
    return render(request,'detalleArtista.html',contexto)
def listaCanciones(request):
    canciones = Cancion.objects.order_by('id')
    nombre_canciones = ', '.join([cancion.nombre for cancion in canciones])
    return HttpResponse(nombre_canciones)

def detalleCancion(request,id_cancion):
    try:
        cancion = Cancion.objects.get(pk = id_cancion)
        cadenaDeTexto = f"{cancion.nombre} - ID: {cancion.fechaLanzamiento} - Artista: {cancion.artista}\n"
        return HttpResponse(cadenaDeTexto)
    except cancion.DoesNotExist:
        return HttpResponseNotFound("Cancion no encontrada")