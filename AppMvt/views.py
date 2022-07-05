from django.shortcuts import render
from AppMvt.models import Familiares
from django.http import HttpResponse
# Create your views here.


def familiares(self):

    familiares1= Familiares(nombre="Fernando", apellido="Nicolas", fecha_nacimiento="1961-03-01",parentesco="padre", edad=61)
    familiares1.save() 
    texto1= f"Familiar : {familiares1.nombre} {familiares1.parentesco} edad: {familiares1.edad}\n"
  
    return HttpResponse (texto1)

