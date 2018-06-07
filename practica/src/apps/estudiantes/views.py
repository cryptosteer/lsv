# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def crear(request):
    return HttpResponse("Vamos a CREAR un estudiante")


def borrar(request):
    return HttpResponse("Vamos a BORRAR un estudiante")


def editar(request):
    return HttpResponse("Vamos a EDITAR un estudiante")


def inicio(request):
    contexto = {'nombres': 'Pedro Pablo',
                'apellidos':'Castilla Hurtado'
                }
    return render(request, 'estudiantes/inicio.html', contexto)

