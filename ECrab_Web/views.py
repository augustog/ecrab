#!/usr/bin/python
          # -*- coding: utf-8 -*-

#Agreguè encoding utf-8 para que entienda los caracteres con acento, nada crucial

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #Estabas llamando a la funciòn "template" (que no existe) y no la encontraba porque nunca la definiste o importaste, acá te hice los cambios para que ande
import datetime


# Create your views here.

def home (request):

    now= datetime.datetime.now()
    template = loader.get_template('webhome.html')
    #c = context ({"fecha":'now'}) #Si pones una serie de caracteres entre comillas python lo lee como un string literal, y pasa eso. Si pones 'fecha':'now' la pag siempre va a leer 'hoy es now', y no funca. Lo que querès es pasarle la variable que definiste arriba, por eso haces asi:

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
        } #el context ES un diccionario, no necesitàs construirlo llamando a una funcion (igualmente, esa funcion no existe porque no la definiste ni importaste)
        html = template.render(context, request)
        #para hacer el código más entendible, usá nombres representativos de lo que es cada cosa. Osea, 'template' en lugar de 't'.
        return HttpResponse(html)
    
    except Exception as e:
       return render("<body><p>Error 404</p></body>")

def login(request):

    pass

def listas (request):
   pass

def perfil(request):
   pass

def login_user(request):
    pass


    """ logout(request)
    username = password =''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render_to_response('weblog.html', context_instance=RequestContext(request))"""
"""
@login_required(login_url='/login/')
def main(request):
    ...."""

