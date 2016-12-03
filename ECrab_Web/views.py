#!/usr/bin/python
          # -*- coding: utf-8 -*-

# Imports here.

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import auth
from django.contrib.auth.decorators import login_required 
from django.template import RequestContext
from .models import Post
import datetime

# Create your views here.

#MUESTRA -- NO USAR!

def landing(request):
    return HttpResponse('Landing page. <a href="/home/">Log in </a>') ##TODO: Implement landing page

@login_required(login_url='/login/')
def home (request):

    now= datetime.datetime.now()
    posts = Post.objects.all()[:5]
    template = loader.get_template('webhome.html')
<<<<<<< HEAD
    context = {
        'day': now,
        'posts': posts
        }
    html = template.render(context)

=======
    context = {'day':'123'}
    #context = {'post'}
    html = template.render( context, request)
   
>>>>>>> fef40af2cf1b9d35e5885da6cb11d45c3b97c35a
    return HttpResponse(html)

def post(request):
    pass
	   
def login(request):
    template = loader.get_template('weblog.html')
    #context = {}
    html = template.render()
    return HttpResponse(html)

def login_redirect (request):
    user = auth.authenticate(
    	username=request.POST['username'],
        password=request.POST['password']
        ) # 
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/home/')
    else: 
        return HttpResponseRedirect('/login/')
	
def main(request):
   pass
   
  
def listas (request):
   pass

def perfil(request):

    template = loader.get_template('perfil.html')
    context = {'day':'123',}
    html = template.render(context, request)
   
    return HttpResponse(html)