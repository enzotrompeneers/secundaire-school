from django.contrib import admin
from .models import  Klassen, Richtingen, Leraren, Contact

myModels = [Klassen, Richtingen, Leraren, Contact] # list of models
admin.site.register(myModels) # zichtbaar in admin mode
