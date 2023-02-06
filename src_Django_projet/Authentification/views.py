from django.contrib.auth import get_user_model, login, logout, authenticate # permet de recuperer un objet qui correspond à notre model d'utilisateur 
from django.shortcuts import render, redirect

User = get_user_model()

def signup(request):
    if request.method == "POST":  #(pour récuperer les informations du formulaire) Si on est en présence d'une requete POST:
        #traiter le formulaire
        username = request.POST.get("username") #On recupère les données de l'utilisateur
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password) #On crée l'utilisateur
        login(request, user) #On le connecte
        return redirect('homepage') #On le redirige vers la homepage
        
    
    return render(request,'signup.html')

def login_user(request):
    if request.method == "POST":
        #Connecter l'utilisateur
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('homepage')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('homepage')