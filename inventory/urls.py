from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^$', index, name='index'),

    url(r'^display_voitures$', display_voitures, name='display_voitures'),
    url(r'^display_clients$', display_clients, name='display_clients'),
    url(r'^display_visites$', display_visites, name='display_visites'),

    url(r'^add_voitures$', add_voitures, name='add_voitures'),
    url(r'^add_clients$', add_clients, name='add_clients'),
    url(r'^add_visites$', add_visites, name='add_visites'),
]