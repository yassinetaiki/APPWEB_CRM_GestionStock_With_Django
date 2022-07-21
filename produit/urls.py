#### configuration de l'url produit ####
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='acueill') ,
    path('/afficher_produit',views.afficher_produit,name="afficher_produit")

]