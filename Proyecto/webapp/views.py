from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bienvenido (request):
    return render (request, 'pages/home.html')

def nosotros (request):
    return render (request, 'pages/nosotros.html')

def servicios (request):
    return render (request, 'pages/servicios.html')

def pedidos (request):
    return render (request, 'pages/pedidos.html')