from django.db import models

# Create your models here.

class Usuarios(models.Model):
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class GestionReservaMedica(models.Model):
    nombreCliente = models.CharField(max_length=20)
    apellidoCliente = models.CharField(max_length=20)
    rutCliente = models.CharField(max_length=15)
    telefonoCliente = models.CharField(max_length=10)
    direccionCliente = models.CharField(max_length=200)
    fechaReserva = models.DateField()
    horaReserva = models.TimeField()
    mascotaCliente = models.CharField(max_length=20)

    def __str__(self):
        return self.nombreCliente

class GestionFuncionario(models.Model):
    nombreFuncionario = models.CharField(max_length=20)
    apellidoFuncionario = models.CharField(max_length=20)
    rutFuncionario = models.CharField(max_length=15)
    telefonoFuncionario = models.CharField(max_length=10)
    direccionFuncionario = models.CharField(max_length=200)
    contactoEmergencia = models.CharField(max_length=20)
    telefonoEmergencia = models.CharField(max_length=20)
    

    def __str__(self):
        return self.nombreFuncionario

class GestionInventario(models.Model):
    nombreProducto = models.CharField(max_length=20)
    cantidadProducto = models.CharField(max_length=20)
    fechaCompra = models.DateField()
    nombreProveedor = models.CharField(max_length=10)
    telefonoProveedor = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombreProducto
