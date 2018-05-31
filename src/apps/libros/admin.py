# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from apps.libros.models import Libro, Autor


class AdminAutor(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ciudad', 'genero')


class AdminLibro(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'autor')


admin.site.register(Libro, AdminLibro)
admin.site.register(Autor, AdminAutor)
