from django.http import HttpResponse
from django.shortcuts import render
from.models import Client
from commande.filters import CommandeFiltre
from django.contrib.auth.decorators import login_required



# Create your views here
@login_required(login_url='acces')
def liste_client(request,pk):
    #return HttpResponse('bienvenue client ')
    client=Client.objects.get(id=pk)
    commande=client.commande_set.all()
    total_commande=commande.count()
    mon_filtre=CommandeFiltre(request.GET ,queryset=commande)
    commande=mon_filtre.qs
    context={'client':client,'commande':commande,'total':total_commande,'mon_filtre':mon_filtre}
    return render(request,'client/liste_client.html',context)


def afficher_all_client(request):
    client=Client.objects.all()
    context={'clients':client}
    return render(request,'client/afficher_client.html',context)