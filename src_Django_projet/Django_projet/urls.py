"""Django_projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import page_accueil #On peut également faire un   .views 
from Authentification.views import signup, logout_user, login_user
from RDV.views import prise_rendez_vous, confirmation_rdv
from Django_projet import settings

urlpatterns = [
    path('', page_accueil, name="homepage"),
    path('admin/', admin.site.urls),
    path('signup/', signup, name="signup"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('rendez_vous/', prise_rendez_vous, name="rdv"),
    path('confirmation_rendez_vous/', confirmation_rdv, name='confirmation_rdv')

]
