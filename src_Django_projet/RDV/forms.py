from django import forms
from django.forms import ModelForm, DateInput, TimeInput
from.models import prendre_rendez_vous


# class formulaire_rdv(forms, ):
    
#     date = forms.DateField(label='Date du rendez-vous')
#     heure = forms.TimeField(label='Heure du rendez-vous')
#     Nom = forms.CharField(label='Nom', max_length=100)
#     Téléphone = forms.CharField(label='Téléphone', max_length=20)
#     email = forms.EmailField(label='Email', max_length=100)
#     description = forms.CharField(label='description', max_length=200)

class formulaire_rdv(ModelForm):
    class Meta: # Class meta n'utilise pas des objets mais des class
        model= prendre_rendez_vous # On undique le model que l'on utilise
        fields=["date", "heure", "nom","téléphone","email", "description"] # Les champs que l'on va ajouter sur le formulaire
        widgets = {
            'date': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'heure': TimeInput(attrs={'type': 'time'}, format='%H:%M'),
        }