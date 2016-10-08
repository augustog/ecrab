from django.shortcuts import render

# Create your views here.
#def login(request):
#	pass 
#
#def listas (request):
#	pass
#
#def perfil(request):
#	pass

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

def login (request):

	return render(request, 'weblog.html')

