from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
# Create your views here.

def curso(request):
    curso=Curso(nombre="Python-Django", comision="34640")
    curso.save() #guarda el curso en la base de datos
    cadena_Texto = "Curso guardado: "+curso.nombre+" " + str(curso.comision) #cadena concatenada
    return HttpResponse (cadena_Texto) #muestro lo que estoy guardando