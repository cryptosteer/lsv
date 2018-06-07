# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    autor = models.ForeignKey(Autor)
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    idioma = models.CharField(max_length=50)

    def __str__(self):
       return self.nombre


