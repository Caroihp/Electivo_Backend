from django.shortcuts import render

from rest_framework import viewsets, filters
from .models import Pelicula, Sala, Funcion, Empleado, Boleto
from .serializers import PeliculaSerializer, SalaSerializer, FuncionSerializer, EmpleadoSerializer, BoletoSerializer

# Create your views here.

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo', 'genero']

class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class FuncionViewSet(viewsets.ModelViewSet):
    queryset = Funcion.objects.all()
    serializer_class = FuncionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['pelicula__titulo', 'sala__nombre']
    filterset_fields = ['pelicula', 'sala']

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'rol']
    filterset_fields = ['sala']

class BoletoViewSet(viewsets.ModelViewSet):
    queryset = Boleto.objects.all()
    serializer_class = BoletoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['tipo']
    filterset_fields = ['funcion__pelicula', 'funcion__sala', 'tipo']