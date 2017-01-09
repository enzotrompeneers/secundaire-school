from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    telefoonNr = forms.CharField(equired=True)
    adres = forms.CharField(equired=True)
    bericht = forms.CharField(required=True, widget=forms.Textarea)