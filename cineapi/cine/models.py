from django.db import models

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    duracion_minutos = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo

class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()

    def __str__(self):
        return f'Sala {self.nombre} ({self.capacidad} asientos)'
    #primera - 30
    #Sala Primera (30 asientos)

class Funcion(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return f'Función de {self.pelicula.titulo} en {self.sala.nombre} el {self.fecha_hora.strftime("%Y-%m-%d %H:%M")}'

class Empleado(models.Model):
    ROL_CHOICES = [
        ('gerente', 'Gerente'),
        ('taquillero', 'Taquillero'),
        ('concesionario', 'Concesionario'),
        ('limpieza', 'Limpieza'),
        ('seguridad', 'Seguridad'),
        ('proyeccionista', 'Proyeccionista'),
        ('administrativo', 'Administrativo'),
        ('otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=300)
    rol = models.CharField(max_length=50, choices=ROL_CHOICES)
    sala = models.ForeignKey(Sala, 
                             on_delete=models.SET_NULL, 
                             null=True, 
                             blank=True, 
                             related_name='empleados'
                             )
    
    def __str__(self):
        return f'{self.nombre} ({self.rol}) - Sala: {self.sala.nombre if self.sala else "N/A"}'

class Boleto(models.Model):
    TIPO_CHOICES = [
        ('adulto', 'Adulto'),
        ('nino', 'Nino'),
        ('estudiante', 'Estudiante'),
        ('senior', 'Senior'),
        ('vip', 'VIP'),
    ]
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE, related_name='boletos')
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Boleto {self.tipo} - {self.funcion}'