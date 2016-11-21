from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# ARI: Fijate toda la data que podés agregar al modelo de user uqe viene predefinido,
# cualquier dato que no puedas sacar de ahí, lo agregás a esta clase que te ponog acá
# después te muestro como se usa bien. --A

class ExtendedUser (models.Model):
	'''
	Extended user class,
	este es un approach medio choto, la otra sería heredar de User y extender a voluntad, pero esto es más fácil 
	'''
	user = models.ForeignKey(User)
	#dato = models.XXField()

<<<<<<< HEAD
#class Recordatorio (models.Model):
    #user = models.ForeignKey(User) #Check use of ForeignKey
    #date = models.DateField() #Check attributes
	#done = models.BooleanField() #Check
=======
class Recordatorio (models.Model):
    user = models.ForeignKey(User) #Check use of ForeignKey
    date = models.DateField() #Check attributes
	done = models.BooleanField() #Check

## Pensá qué otras cosas vas a estar manejando con la app, para eso hay que pensar el diagrama de clases.
## Cuando estés para avanzar avisame y lo vemos. -- A

class Proyectos (models.Model):
	name = models.textfield(max_length = 300) #Nombre del Proyecto
	user = models.ForeignKey(User) #Usuario que lo creo
	initdate = models.DateField() #Fecha en la que se inicia el proyecto
	findate = models.DateField() #Fecha en la que finaliza
	#file = ... #El archivo del proyecto
>>>>>>> be4fd39d1e031bddfd28d700fa8a27cea88fef94
