from django import forms
from .models import *

class clientsForm(forms.ModelForm):
    class Meta:
        model = client
        fields = ('nom_client', 'prenom_client', 'mail', 'numtel', 'address')


class voitureForm(forms.ModelForm):
    class Meta:
        model = voiture
        fields = ('matricule', 'date_fabrication', 'id_modele', 'id_client')


class visitesForm(forms.ModelForm):
    class Meta:
        model = visite
        fields = ('id_client', 'id_voiture', 'matricule', 'visite_date', 'id_service', 'visite_prix')
