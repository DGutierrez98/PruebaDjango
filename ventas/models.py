from django.db import models

class productos(models.Model):
    nombre = models.CharField(max_length=100)
    descipcion = models.CharField(max_length=500)
    precio = models.DecimalField(null=True, blank=True, max_digits=40, decimal_places=2)
    fecha_alta = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.nombre)

