from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Usuario(models.Model):
	name = models.TextField(max_length=400)
	lastname = models.TextField(max_length=400)
	username = models.TextField(max_length=400) 
	password = models.TextField(max_length=300)


	