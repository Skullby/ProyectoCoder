from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
from django.template import Template, Context, loader
import datetime

# Create your views here.


def curso(self):
   curso  = Curso(nombre = "Desarrollo Web", camada="19881")
   curso.save()
   documentoDeTexto = f"----> Curso: {curso.nombre}     Camada: {curso.camada}"
   return HttpResponse(documentoDeTexto)

def hola(self):
   juancito = 'juan'
   return HttpResponse(juancito)

def saludo(request):
	return HttpResponse("Hola Django - Coder")

def probandoTemplate(self):
    nom = "Nicolas"
    ap = "Perez"

    listaDeNotas = [2,4,3,7,5,6]

    diccionario = {"nombre" : nom , "apellido" : ap, "hoy ": datetime.datetime.now(), "notas" : listaDeNotas}

    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)


    


