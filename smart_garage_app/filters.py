import django_filters
from django_filters import DateFilter

from .models import *

# Définit les filtres utilisés dans la fonction de recherche. Chaque modèle dispose d'un filtre avec les champs que nous pensons être les plus importants pour réaliser une recherche avec
# VoitureFilter : utilisé pour la recherche sur la table des voitures
# ClientFilter : utilisé pour la recherche sur la table des cliens
# InterventionFilter : utilisé pour la recherche sur la table des Interventions
# TechnicienFilter : utilisé pour la recherche sur la table des techniciens

class VoitureFilter(django_filters.FilterSet):
    startdate = DateFilter(field_name='date_arrivee', lookup_expr='gte')
    enddate = DateFilter(field_name='date_arrivee', lookup_expr='lte')
    class Meta:
        model = Voiture
        fields = '__all__'
        exclude = ['kilometrage', 'type', 'date_arrivee', 'date_fabrication']

class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['prenom']

class InterventionFilter(django_filters.FilterSet):
    startdate = DateFilter(field_name='date_intervention', lookup_expr='gte')
    enddate = DateFilter(field_name='date_intervention', lookup_expr='lte')
    class Meta:
        model = Intervention
        fields = '__all__'
        exclude = ['remarque', 'date_intervention']

class TechnicienFilter(django_filters.FilterSet):
    class Meta:
        model = Intervention
        fields = '__all__'
        exclude = ['nombre_voiture_reparees']