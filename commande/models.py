from django.db import models
from client.models import Client
from produit.models import Produit

# Create your models here.
class Commande(models.Model):
    STATUT=(('en instance' , 'en instance '),
            ('non livre ' , 'non livre'),
            ('livre' , 'livre'))
    client=models.ForeignKey(Client, null=True ,on_delete=models.SET_NULL)
    produit=models.ForeignKey(Produit,null=True, on_delete=models.SET_NULL)
    statut=models.CharField(max_length=200,null=True ,choices=STATUT)
    date_creation=models.DateTimeField(auto_now_add=True,null=True)

