from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def crear(request):
    return HttpResponse('Vamos a CREAR una Aula')


def editar(request):
    return HttpResponse('vamos a EDITAR una aula')


def borrar(request):
    return HttpResponse('vamos a BORRAR una aula')


def inicio(request):
    contexto = {'nombre': 'Aula Master',
                'codigo': '001'
                }
    return render(request, 'aulas/inicio.html', contexto)

