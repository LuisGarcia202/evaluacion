from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def inicio(request):
    return render(request, 'index.html')

def acerca_de(request):
    return HttpResponse("Esta es una página de información acerca de nosotros.")

def contacto(request):
    return HttpResponse("Puedes contactarnos en info@ejemplo.com.")