from __future__ import unicode_literals
from django.db import models

from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS

class Richtingen(models.Model):
    naam = models.CharField(max_length=100)
    omschrijving = models.TextField(max_length=2000)
    def __str__(self):
        return '%s %s' % (self.naam, self.omschrijving)
class Leraren(models.Model):
    naam = models.CharField(max_length=100)
    voornaam = models.CharField(max_length=100)
    foto = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    def __str__(self):
        return '%s %s %s %s' % (self.naam, self.voornaam, self.foto, self.email)

class Klassen(models.Model):
    naam = models.CharField(max_length=100)
    numeriekeCode = models.CharField(max_length=100)
    richting = models.ForeignKey(Richtingen, on_delete=models.CASCADE)
    leeraar = models.ForeignKey(Leraren, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s %s' % (self.naam, self.numeriekeCode, self.richting, self.leeraar)

class Contact(models.Model):
    email = models.EmailField()
    telefoonNr = models.CharField(max_length=20)
    adres = models.CharField(max_length=255)
    bericht = models.TextField(max_length=2000)
    def __str__(self):
        return '%s %s %s %s' % (self.email, self.telefoonNr, self.adres, self.bericht)

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'telefoonNr', 'adres', 'bericht']
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }