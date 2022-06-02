from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('saludo/' , views.saludo),
    path('probandoTemplate/' , views.probandoTemplate),
    # path('curso/', views.curso),
    path('datos/' , views.datos),
    path('mi_plantilla', views.mi_plantilla),
    path('' , views.inicio , name="Inicio"),
    path('cursos/' , views.cursos,  name="Cursos"),
    path('estudiantes/' , views.estudiantes,  name="Estudiantes"),
    path('entregables/' , views.entregables,  name="Entregables"),
    path('profesores/' , views.profesores,  name="Profesores"),
    path('cursoForm/' , views.cursoForm , name='cursoForm'),
    path('cursoFormulario/' , views.cursoFormulario , name="cursoFormulario")

]
