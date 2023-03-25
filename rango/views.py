from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	context={'boldmessage': "Crunchy, creamy, cookie, candy, cupcake"}
	return render(request, 'rango/index.html', context)

def room(request):
	return render(request, 'rango/room.html')

def about(request):
	return render(request, 'rango/about.html')

def contact(request):
	return render(request, 'rango/contact.html')

def product(request):
	return render(request, 'rango/product.html')