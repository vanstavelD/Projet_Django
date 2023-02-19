# Projet_Django

# Système de prise de rendez-vous automatique en ligne pour un coach en développement personnel

## Description

Ce projet est un système de prise de rendez-vous en ligne pour un coach en développement personnel. Le site comprend une page d'accueil qui présente le travail du coach, un système d'authentification pour le coach et ses utilisateurs, un système de prise de rdv avec des contraintes de disponibilité.

## Fonctionnalités

- Page d'accueil présentant le travail du coach
- Système d'authentification pour le coach et ses utilisateurs
- Système de prise de rdv avec des contraintes de disponibilité (le coach ne peut être dans deux rendez-vous en même temps)

## Prérequis

- Python 
- Django

## Installation

1. Clonez le repository : git clone https://github.com/vanstavelD/Projet_Django
2. Naviguez vers le répertoire du projet : /projet_django/Projet_Django/src_Django_project
3. Installez les dépendances : pip install -r requirements.txt
4. Créez la base de données : python manage.py migrate
5. Créez un superutilisateur : python manage.py createsuperuser
6. Lancez le serveur : python manage.py runserver

## Utilisation

1. Accédez au site à l'adresse http://127.0.0.1:8000/
2. Connectez-vous avec un compte utilisateur ou en tant que coach
3. Pour pouvoir accéder à la prise de rendez-vous il faut être inscris ou/et être connecté.

## Auteur

Nom : Vanstavel Dylan

N'hésitez pas à me contacter pour toute question ou suggestion.
