from re import template
from django.shortcuts import render
from AppMvt.models import Familiares
from django.http import HttpResponse
from django.template import *

from django.template import loader

# Create your views here.


def padre(request):

    padre= Familiares(nombre="Fernando", apellido="Nicolas", fecha_nacimiento="1961-03-01",parentesco="Padre", edad=61)
    padre.save() 
    
    plantilla1=loader.get_template('madre.html')
    
    data1 ={"madre": {
        "nombre": padre.nombre,
        "apellido":padre.apellido,
        "fecha_nacimiento":padre.fecha_nacimiento,
        "parentesco":padre.parentesco,
        "edad": padre.edad
        }
    }

    documento1=plantilla1.render(data1)
    return HttpResponse (documento1)
    

def madre(self):

    madre= Familiares(nombre="Marcela", apellido="Oliveira", fecha_nacimiento="1969-12-26",parentesco="Madre", edad=53)
    madre.save() 

    plantilla=loader.get_template('madre.html')
    
    data ={"madre": {
        "nombre": madre.nombre,
        "apellido":madre.apellido,
        "fecha_nacimiento":madre.fecha_nacimiento,
        "parentesco":madre.parentesco,
        "edad": madre.edad
        }
    }

    documento=plantilla.render(data)
    return HttpResponse (documento)

def primo(self):
    primo= Familiares(nombre="Juan", apellido="Oliveira", fecha_nacimiento="1996-11-07",parentesco="Primo", edad=26)
    primo.save() 
    plantilla3=loader.get_template('madre.html')
    
    data3 ={"madre": {
        "nombre": primo.nombre,
        "apellido":primo.apellido,
        "fecha_nacimiento":primo.fecha_nacimiento,
        "parentesco":primo.parentesco,
        "edad": primo.edad
        }
    }

    documento3=plantilla3.render(data3)
    return HttpResponse (documento3)

def inicio(self):
    return HttpResponse("vista de inicio")