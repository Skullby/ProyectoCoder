from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('saludo/' , views.saludo),
    path('probandoTemplate/' , views.probandoTemplate),
    path('cursos/', views.curso),
    path('hola/' , views.hola),
]