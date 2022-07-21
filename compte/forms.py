from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User #importer le modele pour les champs utilisateur
from django import forms #importer formulaire

class CreerUtilisateur(UserCreationForm): #creerutulisateur il herite de usercreationform
    class Meta:
        model=User #le model dans ce cas ca sera user avec ces chmaps predifinie
        fields=['username','email','password1','password2'] #champs deja definie
