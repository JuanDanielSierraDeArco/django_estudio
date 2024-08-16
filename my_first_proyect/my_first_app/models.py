from django.db import models

# Definición del modelo Car
class Car(models.Model):
    # Campo para el título del coche, con una longitud máxima de 250 caracteres
    title = models.CharField(max_length=250)
