from django.shortcuts import render
from django.http import HttpResponse

from .models import Klassen, Richtingen, Leraren, Contact

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
def richtingen(request):
    alleRichtingen = Richtingen.objects.all()
    return render(request, 'crud/richtingen.html', {'alleRichtingen': alleRichtingen})
def leraren(request):
    alleLeraren = Leraren.objects.all()
    return render(request, 'crud/leraren.html', {'alleLeraren': alleLeraren})
def klassen(request):
    alleKlassen = Klassen.objects.all()
    return render(request, 'crud/klassen.html', {'alleKlassen': alleKlassen})