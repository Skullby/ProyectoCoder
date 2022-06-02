from django import forms

class cursoForm(forms.Form):
    nombre = forms.CharField(max_length = 40)
    camada = forms.IntegerField()

class estudianteForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()

class profesorForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class entregableForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    fechaDeEntrega = forms.DateField()  
    entregado = forms.BooleanField()
    