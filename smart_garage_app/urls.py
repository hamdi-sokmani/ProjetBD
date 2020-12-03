from django.conf.urls import url
from .views import *
from .forms import *

urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^display_voitures$', display_voitures, name='display_voitures'),
    url(r'^display_clients$', display_clients, name='display_clients'),
    url(r'^display_techniciens', display_techniciens, name='display_techniciens'),
    url(r'^display_interventions$', display_interventions, name='display_interventions'),

    url(r'^add_voitures$', add_voitures, name='add_voitures'),
    url(r'^add_clients$', add_clients, name='add_clients'),
    url(r'^add_techniciens$', add_techniciens, name='add_techniciens'),
    url(r'^add_interventions$', add_interventions, name='add_interventions'),
    url(r'^add_communes$', add_communes, name='add_communes'),

    url(r'^edit_voitures/(?P<pk>\d+)$', edit_voitures, name='edit_voitures'),
    url(r'^edit_clients/(?P<pk>\d+)$', edit_clients, name='edit_clients'),
    url(r'^edit_interventions/(?P<pk>\d+)$', edit_interventions, name='edit_interventions'),
    url(r'^edit_techniciens/(?P<pk>\d+)$', edit_techniciens, name='edit_techniciens'),
    url(r'^edit_communes/(?P<pk>\d+)$', edit_communes, name='edit_communes'),
    url(r'^edit_typeReparition/(?P<pk>\d+)$', edit_typeReparition, name='edit_typeReparition'),

    url(r'^delete_voitures/(?P<pk>\d+)$', delete_voitures, name='delete_voitures'),
    url(r'^delete_clients/(?P<pk>\d+)$', delete_clients, name='delete_clients'),
    url(r'^delete_interventions/(?P<pk>\d+)$', delete_interventions, name='delete_interventions'),
    url(r'^delete_techniciens/(?P<pk>\d+)$', delete_techniciens, name='delete_techniciens'),
    url(r'^delete_communes/(?P<pk>\d+)$', delete_communes, name='delete_communes'),
    url(r'^delete_typeReparition/(?P<pk>\d+)$', delete_typeReparition, name='delete_typeReparition'),
]