from django.shortcuts import render, render_to_response, redirect
from .models import *
from django.contrib.auth import authenticate, login
# Create your views here.

def principal(request):
    return render_to_response("app/index.html", locals())

def alumnos(request):
    alumnos = Estudiante.objects.all()
    return render_to_response("app/alumnos.html", locals())
def articulos(request):
    articulos = Articulo.objects.all()
    return render_to_response("app/articulos.html", locals())

def prestamos(request):
    prestamos = DetallePrestamo.objects.all()
    return render_to_response("app/prestamo.html", locals())