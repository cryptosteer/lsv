# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def crear(request):
    return HttpResponse("Vamos a CREAR un profesor")


def borrar(request):
    return HttpResponse("Vamos a BORRAR un profesor")


def editar(request):
    return HttpResponse("Vamos a EDITAR un profesor")

def inicio(request):
    return render(request,'profesores/inicio.html')

def inicio(request):
    contexto = {'nomprofesor':'Kacaroto',
                'materdicta':'La teletransportaciòn'
                }
    return render(request,'profesores/inicio.html', contexto)
