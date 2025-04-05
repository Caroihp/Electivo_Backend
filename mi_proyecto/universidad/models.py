from django.db import models

# Create your models here.

class Universidad(models.Model):
    nombre_universidad = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_universidad} - {self.ciudad}"


class Curso(models.Model):
    nombre_curso = models.CharField(max_length=100)
    creditos = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre_curso} ({self.creditos} créditos)"


class Estudiante(models.Model):
    nombre_estudiante = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_estudiante} ({self.correo})"


class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudiante.nombre_estudiante} inscrito en {self.curso.nombre_curso} el {self.fecha_inscripcion}"
