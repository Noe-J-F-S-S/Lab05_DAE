import email
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Clategoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Clategoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock =models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    dni = models.IntegerField(default=0)
    teléfono = models.IntegerField(default=0)
    dirección = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fecha_nac = models.DateField()
    pub_date =models.DateTimeField('date published')

    def __str__(self):
        return self.nombres