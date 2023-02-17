from django.db import models
from Authentification.models import user
# Modèle de rendez-vous 
class prendre_rendez_vous(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    description = models.TextField(max_length=200)
    nom = models.CharField(max_length=100)
    téléphone = models.CharField(max_length=20)
    email = models.EmailField()
    
    
    # définir une représentation sous forme de chaîne de caractères pour chaque rendez-vous. Cela sera utile lorsqu'on va afficher une liste de rendez-vous dans l'interface d'administration Django
    def __str__(self): 
        return f"rendez-vous du {self.date} à {self.heure} avec {self.nom}"