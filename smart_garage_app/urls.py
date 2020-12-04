from django.conf.urls import url
from django.urls import path
from .views import *
from .forms import *

# Définit les urls que nous utilisons dans notre application (Complément de smart_garage/urls.py) 
# Chaque url est liée à une fonction dans view.py que django utilise pour reconnaître le type de fonction qu'il va exécuter pour chaque url utilisée
# On utilise les expressions régulièrers pour reconnaitre les urls
# ^$ : reconnaît les lien type https://127.0.0.1:8000/
# register/ : pour l'inscription
# login et logout : pour la connection et la déconnection
# responsable: la page de l'admin définit par nous
# ^add_voitures$ : reconnaît les lien type https://127.0.0.1:8000/add_voitures
# ...
# ^edit_voitures$ : reconnaît les lien type https://127.0.0.1:8000/edit_voitures/<clé primaire d'une ligne de table>
# ...

urlpatterns = [
    url(r'^$', index, name='index'),

    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('responsable/', responsablePage, name='responsable'),
    
    url(r'^add_voitures$', add_voitures, name='add_voitures'),
    url(r'^add_clients$', add_clients, name='add_clients'),
    url(r'^add_techniciens$', add_techniciens, name='add_techniciens'),
    url(r'^add_interventions$', add_interventions, name='add_interventions'),

    url(r'^edit_voitures/(?P<pk>\w+)$', edit_voitures, name='edit_voitures'),
    url(r'^edit_clients/(?P<pk>\d+)$', edit_clients, name='edit_clients'),
    url(r'^edit_interventions/(?P<pk>\d+)$', edit_interventions, name='edit_interventions'),
    url(r'^edit_techniciens/(?P<pk>\d+)$', edit_techniciens, name='edit_techniciens'),

    url(r'^delete_voitures/(?P<pk>\w+)$', delete_voitures, name='delete_voitures'),
    url(r'^delete_clients/(?P<pk>\d+)$', delete_clients, name='delete_clients'),
    url(r'^delete_interventions/(?P<pk>\d+)$', delete_interventions, name='delete_interventions'),
    url(r'^delete_techniciens/(?P<pk>\d+)$', delete_techniciens, name='delete_techniciens'),
]
