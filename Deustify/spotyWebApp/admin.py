from django.contrib import admin # type: ignore
from .models import Genero,Artista,Cancion
# Register your models here.

class GeneroAdmin(admin.ModelAdmin):
    fieldsets=[
        ('ID',{'fields':['id']}),
        ('Nombre del genero',{'fields':['nombre']}),
        ('Origen del genero',{'fields':['origen']})
    ]

admin.site.register(Genero,GeneroAdmin)

class ArtistaAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Informacion sobre el artista',{'fields':['id','nombre','fechaNacimiento','imagen_url']}),
        ('Genero al que pertenece',{'fields':['genero']})
    ]

admin.site.register(Artista,ArtistaAdmin)

class CancionAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Informacion sobre la cancion',{'fields':['nombre','fechaLanzamiento','imagen_url']}),
        ('Creada por el artista',{'fields':['artista']})
    ]
admin.site.register(Cancion,CancionAdmin)

