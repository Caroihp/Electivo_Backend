from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PeliculaViewSet, SalaViewSet, FuncionViewSet, EmpleadoViewSet, BoletoViewSet

router = DefaultRouter()
router.register(r'peliculas', PeliculaViewSet)
router.register(r'salas', SalaViewSet)
router.register(r'funciones', FuncionViewSet)
router.register(r'empleados', EmpleadoViewSet)
router.register(r'boletos', BoletoViewSet)

urlpatterns = [
    path('', include(router.urls))
]