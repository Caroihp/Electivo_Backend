from django.contrib import admin
from .models import Pelicula, Sala, Funcion, Empleado, Boleto

# Register your models here.

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'duracion_minutos')
    search_fields = ('titulo', 'genero')

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad')
    search_fields = ('nombre',)

@admin.register(Funcion)
class FuncionAdmin(admin.ModelAdmin):
    list_display = ('pelicula', 'sala', 'fecha_hora')
    search_fields = ('pelicula__titulo', 'sala__nombre')
    list_filter = ('fecha_hora',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rol', 'sala')
    search_fields = ('nombre', 'rol')
    list_filter = ('rol', 'sala')

@admin.register(Boleto)
class BoletoAdmin(admin.ModelAdmin):
    list_display = ('funcion', 'tipo', 'precio', 'fecha_compra')
    search_fields = ('funcion__pelicula__titulo', 'tipo')
    list_filter = ('tipo', 'fecha_compra')
