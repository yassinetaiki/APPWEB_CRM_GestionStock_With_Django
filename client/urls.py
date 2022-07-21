from django.urls import path
from . import views

urlpatterns =[
    path('/<str:pk>/', views.liste_client ,name="client"),
    path('client',views.afficher_all_client,name='afficher_client')
]