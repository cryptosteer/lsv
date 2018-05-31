# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def inicio (request):
    return render(request, 'libros/index.html')


def crear (request):
    return render(request, 'libros/crear.html')


def actualizar (request):
    return render(request, 'libros/actualizar.html')


def borrar (request):
    return render(request, 'libros/borrar.html')