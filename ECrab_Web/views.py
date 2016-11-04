#!/usr/bin/python
          # -*- coding: utf-8 -*-

# Imports here.

from django.contrib.auth.models import Usuario
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from forms import SignUpForm 
import datetime

# Create your views here.

def home (request):

    now= datetime.datetime.now()
    template = loader.get_template('webhome.html')
    
    try:
        context = {
        'fecha': now,
        #'rec1': recordatorio1, 
        #'rec2': recordatorio2,
        #'rec3': recordatorio3,
        #'rec4': recordatorio4,
        #'rec5': recordatorio5,
        #'rec6': recordatorio6,
        #'rec7': recordatorio7,
        } 
        html = template.render(context, request)
       
        return HttpResponse(html)
    
    except Exception as e:
       return render("<body><p>Error 404</p></body>")

def login(request):

    template = loader.get_template('weblog.html')
    #context = {}

    try:

        html = template.render(request)
        return HttpResponse(html)

    except Exception as e:
        return render("<body><p>Error 404</p></body>")

def login_user(request):
 logout(request)
    username = password =''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render_to_response('weblog.html', context_instance=RequestContext(request))
@login_required(login_url='/login/')


def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
 
            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            name = form.cleaned_data["name"]
            lastname = form.cleaned_data["lastname"]
 
            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
 
            # Save new user attributes
            user.save()
 
            return HttpResponseRedirect(reverse('main'))  # Redirect after POST
    else:
        form = SignUpForm()
 
    data = {
        'form': form,
    }
    return render_to_response('signup.html', data, context_instance=RequestContext(request))


def main(request):
   pass

def listas (request):
   pass

def perfil(request):
   pass
