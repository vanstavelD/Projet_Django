from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .forms import formulaire_rdv
from .models import prendre_rendez_vous

def prise_rendez_vous(request):
    if request.method == "POST": # Si la méthode utilisée est POST
        form = formulaire_rdv(request.POST) #Alors nous créons une insatnce de notre formulaire en lui passant les données soumises dans la requête 
        if form.is_valid(): # On vérifie si le formulaire est valide avec la méthode is_valid()
            
            
            # Si le formulaire est valide, on récupère les données propres du formulaire avec cleaned_data
            date = form.cleaned_data['date']
            heure = form.cleaned_data['heure']
            nom = form.cleaned_data['nom']
            téléphone = form.cleaned_data['téléphone']
            email = form.cleaned_data['email']
            description = form.cleaned_data['description']
            
            
            # Si il existe déja un rendez-vous à la date et l'heure 
            rendez_vous_deja_pris = prendre_rendez_vous.objects.filter(date=date, heure=heure) # La méthode filter est utilisée pour trouver tous les objets du modèle qui correspondent au critère qu'on lui demande
            if rendez_vous_deja_pris:
                form.add_error(None,"Le créneau horaire est déjà pris")
            else:
                form.save()
                return redirect('confirmation_rdv')
                
            

    else:
        form = formulaire_rdv()
    return render(request, 'rendez_vous.html', {'form': form})
            
def confirmation_rdv(request):
    # if prise_rendez_vous:
        # Récupérer le dernier rendez-vous ajouté à la base de données
        prise_rendez_vous = prendre_rendez_vous.objects.latest('id')
        return render(request,'confirmation_rdv.html',{'prise_rendez_vous': prise_rendez_vous})