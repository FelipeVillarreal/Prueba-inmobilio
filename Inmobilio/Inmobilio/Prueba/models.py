# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.db import models

# Create your models here.


class General(models.Model):
    Tipo= models.CharField(max_length=35)
    Subtipo= models.CharField(max_length=35)
    Direccion= models.CharField(max_length=35)
    Ciudad= models.CharField(max_length=35)
    Departamento= models.CharField(max_length=35)
    Pais= models.CharField(max_length=35)
    Telefono= models.CharField(max_length=35)

    def tipoinmueble(self):
        cadena="{0}, {1}"
        return cadena.format(self.Tipo, self.Subtipo)

    def __str__(self):
       return self.tipoinmueble()


class Interior(models.Model):
    Cuartos = models.FloatField(max_length=50)
    Banios = models.IntegerField(max_length=50)
    Closets = models.IntegerField(max_length=50)
    Calentador = models.BooleanField(default=False)      

    def __str__(self):
        cadena="Cuartos:({0}), Banios:({1}), Closets:({2}), Calentador:({3})"
        return cadena.format(self.Cuartos, self.Banios, self.Closets, self.Calentador)


class Exterior (models.Model):
    Vigilancia = models.CharField(max_length=50)
    Parqueadero = models.CharField(max_length=50)
    Salon_social = models.BooleanField(default=False)
    Numero_pisos = models.IntegerField(max_length=50)


    def __str__(self):
        cadena = " Vigilancia:({0}), Parqueadero:({1}), Closets({2}), Calentador({3})"
        return cadena.format(self.Vigilancia, self.Parqueadero, self.Salon_social, self.Numero_pisos)
