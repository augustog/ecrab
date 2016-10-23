from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def home (request):

    now= datetime.datetime.now()
    t = template ("<body><p>Hoy es {{fecha}}</p></body>")
    c = context ({"fecha":'now'})
    html = t.render(c)
   
    return HttpResponse(html)

#def login(request):
#   pass 
#
#def listas (request):
#   pass
#
#def perfil(request):
#   pass

"""def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render_to_response('login.html', context_instance=RequestContext(request))

@login_required(login_url='/login/')
def main(request):
    ...."""

