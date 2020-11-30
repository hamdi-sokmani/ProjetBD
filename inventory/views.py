from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def display_voitures(request):
    items = voiture.objects.all()
    context = {
        'headers' : ['id', 'Matricule', 'Date de fabrication', 'Modèle', 'Propriétaire'],
        'title' : "Voitures",        
        'items' : items,
    }

    return render(request, 'index.html', context)

def display_clients(request):
    items = client.objects.all()
    context = {
        'headers' : ['id', 'Nom', 'Prénom', 'Mail', 'Numéro du téléphone', 'Addresse'],
        'title' : "Clients",
        'items' : items,
    }

    return render(request, 'index.html', context)

def display_visites(request):
    items = visite.objects.all()
    context = {
        'headers' : ['id', 'Client', 'Voiture', 'Matricule', 'Date de visite', 'Service', 'Prix'],
        'title' : "Visites",
        'items' : items,
    }

    return render(request, 'index.html', context)

def add_element(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls()
        return render(request, 'add_new.html', {'form': form})

def add_voitures(request):
    return add_element(request, voitureForm)

def add_clients(request):
    return add_element(request, clientsForm)

def add_visites(request):
    return add_element(request, visitesForm)