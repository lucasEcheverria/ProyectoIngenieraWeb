from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
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
    genero = get_object_or_404(Genero, pk=id_genero)
    contexto = {'genero': genero}
    return render(request, 'detalleGenero.html', contexto)

def listaArtistas(request):
    artistas = Artista.objects.order_by('nombre')
    nombre_artistas = ', '.join([artista.nombre for artista in artistas])
    return HttpResponse(nombre_artistas)

def detalleArtistas(request, id_artista):
    try:
        artista = Artista.objects.get(pk=id_artista)
        canciones = artista.canciones.all()

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
    canciones = Cancion.objects.order_by('id')
    nombre_canciones = ', '.join([cancion.nombre for cancion in canciones])
    return HttpResponse(nombre_canciones)

def detalleCanciones(request,id_cancion):
    try:
        cancion = Cancion.objects.get(pk = id_cancion)
        cadenaDeTexto = f"{cancion.nombre} - ID: {cancion.fechaLanzamiento} - Artista: {cancion.artista}\n"
        return HttpResponse(cadenaDeTexto)
    except cancion.DoesNotExist:
        return HttpResponseNotFound("Cancion no encontrada")