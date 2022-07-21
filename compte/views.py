from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreerUtilisateur
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def page_inscription(request):
    form=CreerUtilisateur()
    if(request.method=='POST'):
        form=CreerUtilisateur(request.POST)
        if(form.is_valid()):
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"Compte Creer avec success")
            return redirect('acces')
    context = {'form':form}
    return render(request,'compte/inscription.html',context)


def page_acces(request):
    context={}
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None :
            login(request , user)
            return redirect('acueill')
        else:
            messages.info(request,"nom utilisateur et/ou mot de passe incorrecte")


    return render(request,'compte/acces.html',context)


def quitter_page(request):
    logout(request)
    return redirect('acces')