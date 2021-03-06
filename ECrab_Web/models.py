from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ExtendedUser (models.Model):
	
	#Extended user class 
	
	user = models.ForeignKey(User) 
	#dato = models.XXField()

class Recordatorio (models.Model):
    user = models.ForeignKey(User) #Check use of ForeignKey
    date = models.DateField() #Check attributes
    done = models.BooleanField() #Check

class Proyectos (models.Model):
	name = models.TextField(max_length = 300) #Nombre del Proyecto
	user = models.ForeignKey(User) #Usuario que lo creo
	initdate = models.DateField() #Fecha en la que se inicia el proyecto
	findate = models.DateField() #Fecha en la que finaliza
	#file = ... #El archivo del proyecto

class Post (models.Model):
	cont = models.TextField(max_length = 300)
	date = models.DateField()

# Modelo para subir archivos en la base de datos
class Document(models.Model):
	filename = models.CharField(max_length=100)
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')