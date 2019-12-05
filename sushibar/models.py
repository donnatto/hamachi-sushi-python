from django.db import models
from .validators import validate_file_size


class Dish(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=256)
    content = models.TextField(null=True)
    url = models.URLField(null=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Reserva(models.Model):
    nombre = models.CharField(max_length=256)
    apellidos = models.CharField(max_length=256)
    fecha = models.DateField()
    hora = models.TimeField()
    comensales = models.IntegerField()
    nroContacto = models.CharField(max_length=16)
    correo = models.EmailField(max_length=256)

    def __str__(self):
        return self.nombre + ' ' + self.apellidos


class Postulante(models.Model):
    nombre = models.CharField(max_length=256)
    correo = models.EmailField(max_length=256)
    nroContacto = models.CharField(max_length=16)
    cv = models.FileField(upload_to='cv/', validators=[validate_file_size])
    mensaje = models.TextField(null=True)

    def __str__(self):
        return self.nombre


class Mensaje(models.Model):
    nombre = models.CharField(max_length=256)
    correo = models.EmailField(max_length=256)
    asunto = models.CharField(max_length=128)
    mensaje = models.TextField(null=True)

    def __str__(self):
        return self.nombre + ': ' + self.asunto
