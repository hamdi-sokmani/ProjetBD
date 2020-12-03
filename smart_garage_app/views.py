from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def index(request):
    return render(request, 'index.html')

def display_voitures(request):
    items = Voiture.objects.all()
    context = {
        'headers' : ['Matricule', 'Marque', 'Type', 'Date de fabrication', 'Kilométrage', "Date d'arrivée"],
        'title' : "Voitures",        
        'items' : items,
    }

    return render(request, 'index.html', context)
def display_clients(request):
    items = Client.objects.all()
    context = {
        'headers' : ['Numéro', 'Nom', 'Prénom', 'Commune', 'Personne résponsable de la commande'],
        'title' : "Clients",
        'items' : items,
    }

    return render(request, 'index.html', context)
def display_interventions(request):
    items = Intervention.objects.all()
    context = {
        'headers' : ['Voiture', 'Client', 'Technicien', "Date de l'intervention", 'Type de Réparition', 'Remarques du technicien'],
        'title' : "Interventions",
        'items' : items,
    }

    return render(request, 'index.html', context)
def display_techniciens(request):
    items = Technicien.objects.all()
    context = {
        'headers' : ['Numéro', 'Nom', 'Prénom', 'Nombre des voitures réparées'],
        'title' : "Techniciens",
        'items' : items,
    }
    
    return render(request, 'index.html', context)
def display_communes(request):
    items = Commune.objects.all()
    context = {
        'headers' : ['Nom de la commune', 'Nombre du client dans la commune'],
        'title' : "Communes",
        'items' : items,
    }

    return render(request, 'index.html', context)
def display_types_reparition(request):
    items = TypeReparition.objects.all()
    context = {
        'headers' : ['Type', 'Nom', 'Détails'],
        'title' : "TypesRéparition",
        'items' : items,
    }

    return render(request, 'index.html', context)


def add_elements(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls()
        return render(request, 'add_new.html', {'form': form})

def add_voitures(request):
    return add_elements(request, voitureForm)
def add_clients(request):
    return add_elements(request, clientForm)
def add_interventions(request):
    return add_elements(request, interventionForm)
def add_techniciens(request):
    return add_elements(request, technicienForm)
def add_communes(request):
    return add_elements(request, communeForm)
# pas de add_réparition


def edit_elements(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})

def edit_voitures(request, pk):
    return edit_elements(request, pk, Voiture, voitureForm)
def edit_clients(request, pk):
    return edit_elements(request, pk, Client, clientForm)
def edit_interventions(request, pk):
    return edit_elements(request, pk, Intervention, interventionForm)
def edit_techniciens(request, pk):
    return edit_elements(request, pk, Technicien, technicienForm)
def edit_communes(request, pk):
    return edit_elements(request, pk, Commune, communeForm)
def edit_typeReparition(request, pk):
    return edit_elements(request, pk, TypeReparition, typeReparitionForm)

def delete_voitures(request, pk):

    Voiture.objects.filter(pk=pk).delete()

    items = Voiture.objects.all()

    context = {
        'headers' : ['Matricule', 'Marque', 'Type', 'Date de fabrication', 'Kilométrage', "Date d'arrivée"],
        'title' : "Voitures",        
        'items' : items,
    }

    return render(request, 'index.html', context)
def delete_clients(request, pk):

    Client.objects.filter(pk=pk).delete()

    items = Client.objects.all()

    context = {
        'headers' : ['Numéro', 'Nom', 'Prénom', 'Commune', 'Personne résponsable de la commande'],
        'title' : "Clients",
        'items' : items,
    }

    return render(request, 'index.html', context)
def delete_interventions(request, pk):

    Intervention.objects.filter(pk=pk).delete()

    items = Intervention.objects.all()

    context = {
        'headers' : ['Voiture', 'Client', 'Technicien', "Date de l'intervention", 'Type de Réparition', 'Remarques du technicien'],
        'title' : "Interventions",
        'items' : items,
    }

    return render(request, 'index.html', context)
def delete_techniciens(request, pk):

    Technicien.objects.filter(pk=pk).delete()

    items = Technicien.objects.all()

    context = {
        'headers' : ['Numéro', 'Nom', 'Prénom', 'Nombre des voitures réparées'],
        'title' : "Techniciens",
        'items' : items,
    }

    return render(request, 'index.html', context)
def delete_communes(request, pk):

    Commune.objects.filter(pk=pk).delete()

    items = Commune.objects.all()

    context = {
        'headers' : ['Nom de la commune', 'Nombre du client dans la commune'],
        'title' : "Communes",
        'items' : items,
    }

    return render(request, 'index.html', context)
def delete_typeReparition(request, pk):

    TypeReparition.objects.filter(pk=pk).delete()

    items = TypeReparition.objects.all()

    context = {
        'headers' : ['Type', 'Nom', 'Détails'],
        'title' : "TypesRéparition",
        'items' : items,
    }

    return render(request, 'index.html', context)
