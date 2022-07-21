from django.shortcuts import render
from django.http import HttpResponse
from commande.models import Commande
from produit.models import Produit
from client.models import Client
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='acces')
def home(request):
    commandes=Commande.objects.all()
    clients=Client.objects.all()
    context={'commandes':commandes,'clients':clients}
    return render(request,'produit/acueill.html',context)

def afficher_produit(request):
    produit=Produit.objects.all()
    context={'produits':produit}
    return render(request,'produit/afficher_produit.html',context)