from django.db import models

class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    kilometraje = models.PositiveIntegerField()
    fecha_llegada = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"