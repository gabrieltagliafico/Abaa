from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Ventas = 'Ventas'
    Metrologia = 'Matrologia'
    Direccion = 'Direccion'
    Compras = 'Compras'
    cargoChoices = [
        (Ventas, 'Ventas'),
        (Metrologia, 'Metrologia'),
        (Direccion, 'Direccion'),
        (Compras, 'Compras'),
    ]
    cargo= models.CharField(choices=cargoChoices, max_length=15)
