# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def crear(request):
    return HttpResponse("Vamos a CREAR un materia")


def borrar(request):
    return HttpResponse("Vamos a BORRAR un materia")


def editar(request):
    return HttpResponse("Vamos a EDITAR un materia")


def notas(request):
    return HttpResponse("Vamos a ingresar las notas")

def inicio(request):
    contexto = {'nommateria':'La fusion',
                'creditos':'12'
                }
    return render(request,'materias/inicio.html', contexto)