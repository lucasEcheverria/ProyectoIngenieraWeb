from django.urls import path

from . import views


urlpatterns = [
    path('',views.index,name = 'index'),
    path('generos',views.listaGeneros, name= 'listaGeneros'),
    path('generos/<int:id_genero>/', views.detalleGeneros, name='detalleGenero'),
    path('canciones',views.listaCanciones, name= 'listaCanciones'),
    path('artistas',views.listaArtistas, name= 'listaArtistas'),
    path('artistas/<int:id_artista>/', views.detalleArtistas, name='detalleArtista'),
]