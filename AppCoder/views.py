from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Familiares
from django.template import Template, Context, loader
import datetime

# Create your views here.


def curso(self):
   curso  = Curso(nombre = "Desarrollo Web", camada="19881")
   curso.save()
   documentoDeTexto = f"----> Curso: {curso.nombre}     Camada: {curso.camada}"
   return HttpResponse(documentoDeTexto)

def datos(self):
   familiares = Familiares( nombre = "Nicolas" , numero = 7 , fechaDeNac = "2001-1-27")
   familiares.save()
   # documentoDeTexto = f"Nombre: {familiares.nombre} \n Numero: {familiares.numero} \n Cumpleanios:{familiares.fechaDeNac}"
   diccionario = {"nombre":familiares.nombre, "numero":familiares.numero, "fecha":familiares.fechaDeNac}

   plantilla = loader.get_template('template_familiares.html')

   documento = plantilla.render(diccionario)

   return HttpResponse(documento)

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

def inicio(request):

      return render(request, "AppCoder/inicio.html")

def cursos(request):

      return render(request, "AppCoder/cursos.html")

def profesores(request):

      return render(request, "AppCoder/profesores.html")


def estudiantes(request):

      return render(request, "AppCoder/estudiantes.html")


def entregables(request):

      return render(request, "AppCoder/entregables.html")

    


