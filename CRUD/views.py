from django.shortcuts import render
from django.http import HttpResponse
from models import Klassen, Richtingen, Leraren, Contact

def home(request):
    return render(request, 'crud/index.html')
def aanbod(request):
    alleRichtingen = Richtingen.objects.all()
    return render(request, 'crud/aanbod.html', {'alleRichtingen': alleRichtingen})
def wie(request):
    alleLeraren = Leraren.objects.all()
    return render(request, 'crud/wie.html', {'alleLeraren': alleLeraren})

def contact(request):
    return render(request, 'crud/contact.html') #, {'form': form_class}) #grab form and passing it over into the template

def create(request): 
	return render(request, 'crud/create.html')
def read(request): 
	alle_autos = Autos.objects.all()
	return render(request, 'crud/index.html', {'alle_autos': alle_autos})
def update(request): 
	return render(request, 'crud/update.html')
def delete(request): 
	return render(request, 'crud/delete.html')
