from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class clientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('numero', 'nom', 'prenom', 'addresse', 'nom_personne_en_charge')


class voitureForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = ('matricule', 'marque', 'type', 'date_fabrication', 'kilometrage', 'date_arrivee')


class interventionForm(forms.ModelForm):
    class Meta:
        model = Intervention
        fields = ('matricule_voiture', 'numero_client', 'numero_technicien', 'date_intervention', 'type_reparition', 'remarque')


class technicienForm(forms.ModelForm):
    class Meta:
        model = Technicien
        fields = ('numero', 'nom', 'prenom', 'nombre_voiture_reparees')


class communeForm(forms.ModelForm):
    class Meta:
        model = Commune
        fields = ('nom', 'nombre_client')


class typeReparitionForm(forms.ModelForm):
    class Meta:
        model = TypeReparition
        fields = ('type', 'nom', 'details')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
