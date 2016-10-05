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

def saludo (request):

	nombre = "ECrab"
	pagina = "ecrab.com"
	tupla = (1,2,3,4,5,6,7,8,9,10)
		context = {
		'saludo': 'somos geniales',
		'nombre': nombre,
		'tupla': tupla,
	}
	return render(request, 'saludo.html', context)