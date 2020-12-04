from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection 
from .models import *
from .forms import *
from .filters import *
from .decorators import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

from django.contrib import messages

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    items_clients = Client.objects.all()
    items_voitures = Voiture.objects.all()
    items_interventions = Intervention.objects.all()

    cursor = connection.cursor() 
    cursor.execute("SELECT count(*) FROM Client") 
    nbr_total_clients = cursor.fetchone()[0]
    cursor.execute("SELECT count(*) FROM Voiture") 
    nb_total_voitures = cursor.fetchone()[0]
    cursor.execute("SELECT count(*) FROM Intervention") 
    nb_total_interventions = cursor.fetchone()[0]

    myVoitureFilter = VoitureFilter(request.GET, queryset=items_voitures)
    myClientFilter = ClientFilter(request.GET, queryset=items_clients)
    myInterventionFilter = InterventionFilter(request.GET, queryset=items_interventions)

    items_clients = myClientFilter.qs
    items_voitures = myVoitureFilter.qs
    items_interventions = myInterventionFilter.qs

    context = {
        'items_clients' : items_clients,
        'items_voitures' : items_voitures,
        'items_interventions' : items_interventions,
        'total_client' : nbr_total_clients,
        'total_voiture' : nb_total_voitures,
        'total_intervention' : nb_total_interventions,
        'voiture_filter': myVoitureFilter,
        'client_filter': myClientFilter,
        'intervention_filter': myInterventionFilter
    }    
    return render(request, 'index.html', context)

@login_required(login_url='login')
@responsable_role
def responsablePage(request):
    items_techniciens = Technicien.objects.all()

    cursor = connection.cursor() 
    cursor.execute("SELECT count(*) FROM Technicien") 

    myTechnicienFilter = TechnicienFilter(request.GET, queryset=items_techniciens)

    nbr_total_techniciens = cursor.fetchone()[0]

    items_techniciens = myTechnicienFilter.qs

    context = {
        'items_technicien' : items_techniciens,
        'technicien_filter' : TechnicienFilter,
        'total_technicien' : nbr_total_techniciens, 

    }

    return render(request, 'responsable.html', context)

@unauthenticated_user
def registerPage(request):
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='technicien')
            user.group.add(group)

            messages.success(request, 'Compte créé pour ' + username)

            return redirect('login')

    context = {'form':form}
    return render(request, 'register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Le nom d'utilisateur ou le mot de passe est incorrect")

    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def add_elements(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'add_new.html', {'form': form})

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

@login_required(login_url='login')
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

@login_required(login_url='login')
def delete_elements(request, pk, model):
    model.objects.filter(pk=pk).delete()
    items = model.objects.all()

    items_clients = Client.objects.all()
    items_voitures = Voiture.objects.all()
    items_interventions = Intervention.objects.all()
    items_techniciens = Technicien.objects.all()


    context = {      
        'items' : items,
        'items_clients' : items_clients,
        'items_voitures' : items_voitures,
        'items_interventions' : items_interventions,
        'items_techniciens' : items_techniciens
    }
    return render(request, 'index.html', context)

def delete_voitures(request, pk):
    return delete_elements(request, pk, Voiture)
def delete_clients(request, pk):
    return delete_elements(request, pk, Client)
def delete_interventions(request, pk):
    return delete_elements(request, pk, Intervention)
def delete_techniciens(request, pk):
    return delete_elements(request, pk, Technicien)