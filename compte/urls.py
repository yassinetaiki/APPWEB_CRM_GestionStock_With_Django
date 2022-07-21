from django.urls import path
from . import views

urlpatterns = [
    path('/inscription',views.page_inscription,name='inscription'),
    path('/acces',views.page_acces,name='acces'),
    path('/quitter',views.quitter_page,name='quitter'),
]