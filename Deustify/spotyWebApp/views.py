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

def detalleGenero(request, id_genero):
    genero = get_object_or_404(Genero, pk=id_genero)
    contexto = {'genero': genero}
    return render(request, 'detalleGenero.html', contexto)

def listaArtistas(request):
    artistas = Artista.objects.order_by('nombre')
    contexto = {'artistas' : artistas}
    return render(request, 'listaArtista.html', contexto)

def detalleArtista(request, id_artista):
    artista = get_object_or_404(Artista,pk=id_artista)
    contexto = {'artista':artista}
    return render(request,'detalleArtista.html',contexto)

def listaCanciones(request):
    canciones = Cancion.objects.order_by('nombre')
    contexto = {'canciones' : canciones}
    return render(request, 'listaCancion.html', contexto)

def detalleCancion(request,id_cancion):
    cancion = get_object_or_404(Cancion,pk=id_cancion)
    contexto = {'cancion':cancion}
    return render(request,'detalleCancion.html',contexto)
def index(request):
    generos = Genero.objects.order_by('nombre')
    artistas = Artista.objects.order_by('nombre')
    canciones = Cancion.objects.order_by('nombre')
    contexto = {"generos" : generos, "artistas":artistas,"canciones":canciones}
    return render(request,'index.html',contexto)