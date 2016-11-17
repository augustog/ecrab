#!/usr/bin/python
          # -*- coding: utf-8 -*-

# Imports here.

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from forms import SignUpForm 
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

#MUESTRA -- NO USAR!

def landing(request):
    return HttpResponse('Landing page. <a href="/home/">Log in </a>') ##TODO: Implement landing page
			
@login_required(login_url='/login/')
def home (request):

    now= datetime.datetime.now()
    template = loader.get_template('webhome.html')
    context = {}
    html = template.render(context, request)
   
    return HttpResponse(html)
	   	   
	   
def login(request):

    template = loader.get_template('weblog.html')
    #context = {}
    html = template.render(request)
    return HttpResponse(html)

	   
def login_redirect (request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    ) # 
    if user is not None:
        login(request, user)
        HttpResponseRedirect('/home/')
    else: 
        HttpResponseRedirect('/login/')
		
		
		

def main(request):
   pass
   
  
def listas (request):
   pass

def perfil(request):
   pass
