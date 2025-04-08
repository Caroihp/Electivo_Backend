from django.contrib import admin
from .models import Universidad, Curso, Estudiante, Matricula

# Register your models here.

admin.site.register(Universidad)
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Matricula)