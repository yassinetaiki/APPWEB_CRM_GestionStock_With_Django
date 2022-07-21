from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CommandeForm
from commande.models import Commande
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='acces')
def liste_commande(request):
    #return HttpResponse('liste de commande ')
    commande=Commande.objects.all()
    context={'commandes':commande}
    return render(request,'commande/liste_commande.html',context)


def ajouter_commande(request):
    form=CommandeForm()
    if request.method=='POST':
        form=CommandeForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('/')

    context={'form':form}
    return render(request,'commande/ajouter_commande.html',context)


def modifier_commande(request,pk):
    commande=Commande.objects.get(id=pk)
    form=CommandeForm(instance=commande)

    if request.method=='POST':
        form=CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'commande/modifier_commande.html',context)


def supp_commande(request,pk):
    commande=Commande.objects.get(id=pk)
    if request.method=='POST':
        commande.delete()
        return redirect('/')

    context={'item':commande}
    return render(request,'commande/supprimer_commande.html',context)