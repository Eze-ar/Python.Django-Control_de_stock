from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=8, decimal_places=2) #elijo usar Decimal y no Float para evitar problemas
    stock_actual = models.IntegerField()                         #de precisión
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

