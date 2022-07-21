from django.urls import path
from . import views

urlpatterns=[
    path('afficher_commande/',views.liste_commande,name='afficher_commande'),
    path('ajouter_commande/',views.ajouter_commande,name='ajouter_commande'),
    path('modifier_commande/<str:pk>',views.modifier_commande,name='modifier_commande'),
    path('supprimer_commande/<str:pk>',views.supp_commande,name='supprimer_commande'),
]