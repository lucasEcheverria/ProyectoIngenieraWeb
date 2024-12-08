from django.urls import path
from . import views
from spotyWebApp.views import ListaGeneroView,DetalleGeneroView,ListaCancionesView,DetalleCancionView, DetalleArtistaView, ListaArtistasView
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('',views.index,name = 'index'),
    path('generos',ListaGeneroView.as_view(), name= 'listaGeneros'),
    path('generos/<int:id_genero>/', DetalleGeneroView.as_view(), name='detalleGenero'),
    path('canciones',ListaCancionesView.as_view(), name= 'listaCanciones'),
    path('canciones/<int:id_cancion>/',DetalleCancionView.as_view(), name= 'detalleCancion'),
    path('artistas',ListaArtistasView.as_view(), name= 'listaArtistas'),
    path('artistas/<int:id_artista>/', DetalleArtistaView.as_view(), name='detalleArtista'),

]