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
    texto1= f"Familiar : {padre.nombre} {padre.apellido},\n{padre.parentesco} su edad: {padre.edad}\n"
    
    miHtml = open("C:/Users/Gaspar/Desktop/virtualStudio/mvt/ProyectoMvt/AppMvt/templates/AppMvt/padre.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto= Context(texto1)

    documento=plantilla.render(miContexto)
    return HttpResponse (documento)

def madre(self):

    madre= Familiares(nombre="Marcela", apellido="Oliveira", fecha_nacimiento="1969-12-26",parentesco="Madre", edad=53)
    madre.save() 
    texto2= f"Familiar : {madre.nombre} {madre.apellido} , {madre.parentesco} su edad: {madre.edad}\n"
  
    plantilla=loader.get_template('madre.html')
    
    documento=plantilla.render(texto2)
    return HttpResponse (documento)

def primo(self):

    primo= Familiares(nombre="Juan", apellido="Oliveira", fecha_nacimiento="1996-11-07",parentesco="Primo", edad=26)
    primo.save() 
    texto3= f"Familiar : {primo.nombre} {primo.apellido} , {primo.parentesco} su edad: {primo.edad}\n"
  
    return HttpResponse (texto3)

def inicio(self):
    return HttpResponse("vista de inicio")