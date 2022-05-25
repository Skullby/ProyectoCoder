from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('saludo/' , views.saludo),
    path('probandoTemplate/' , views.probandoTemplate),
    path('curso/', views.curso),
    path('datos/' , views.datos),

]
