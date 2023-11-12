from django.urls import path
from . import views

urlpatterns = [
    # Page d'accueil
    path('', views.index, name='index'),

]


