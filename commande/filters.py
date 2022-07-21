import django_filters #on importe le filtre
from .models import Commande

class CommandeFiltre(django_filters.FilterSet):
    class Meta:
        model=Commande
        fields=('produit','statut')
