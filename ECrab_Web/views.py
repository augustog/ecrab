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

def login (request):

	return render(request, 'weblog.html')
