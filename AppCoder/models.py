from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=30)
    comision=models.IntegerField()

    def __str__(self):
        return self.nombre + " " + self.comision

class Estudiante(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()

    def __str__(self):
        return self.nombre+ " " + self.apellido

class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre+ " " + self.apellido

class Entregable(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    fecha_entrega= models.DateField()
    entregado= models.BooleanField()  #esto es un V o F

    #para chequear si se creo la BD abrimos db browser que nos permite acceder a la info de una BD SQlite