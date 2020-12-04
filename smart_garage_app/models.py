# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# Définit tous les modèles que nous utilisons dans l'application. Django dispose d'un système ORM qui relie automatiquement les champs de nos classes aux tables de la base de données.
# Pour chaque modèle, nous définissons chaque attribut qui est lié à un champ du tableau, y compris les clés primaires et les clés étrangères
# Client : la table des clients
# Commune : la table des communes
# Intervention : la tables des interventions
# Technicien : la table des techniciens
# TypeReparition : la table des types de réparition
# Voiture : la table des voitures

class Client(models.Model):
    numero = models.IntegerField('Numéro', primary_key=True)
    nom = models.CharField('Nom', max_length=20)
    prenom = models.CharField('Prénom', max_length=20)
    addresse = models.ForeignKey('Commune', models.CASCADE, db_column='addresse', verbose_name='Commune du client')
    nom_personne_en_charge = models.CharField('Personne en charge de la commande', max_length=20)

    class Meta:
        managed = False
        db_table = 'client'

    def __str__(self):
        return "{} {}".format(self.nom, self.prenom)


class Commune(models.Model):
    nom = models.CharField('Nom', primary_key=True, max_length=20)
    nombre_client = models.IntegerField('Nombre du client dans la commune', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commune'
    
    def __str__(self):
        return str(self.nom)


class Intervention(models.Model):
    matricule_voiture = models.ForeignKey('Voiture', models.CASCADE, db_column='matricule_voiture', verbose_name='Matricule de la voiture')
    numero_client = models.ForeignKey('Client', models.CASCADE, db_column='numero_client', verbose_name='Numéro du client')
    numero_technicien = models.ForeignKey('Technicien', models.CASCADE, db_column='numero_technicien', verbose_name='Numéro du Technicien')
    date_intervention = models.DateField("Date de l'intervention")
    type_reparition = models.ForeignKey('TypeReparition', models.CASCADE, db_column='type_reparition', verbose_name='Type de réparation')
    remarque = models.TextField('Remarques du technicien', max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'intervention'
    
    def __str__(self):
        return "Intervention à {}".format(self.date_intervention)


class Technicien(models.Model):
    numero = models.IntegerField('Numéro', primary_key=True)
    nom = models.CharField('Nom', max_length=20)
    prenom = models.CharField('Prénom', max_length=20)
    nombre_voiture_reparees = models.IntegerField('Nombre des voitures réparées', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'technicien'
    
    def __str__(self):
        return 'Nº {}: {} {}'.format(self.numero, self.nom, self.prenom)


class TypeReparition(models.Model):
    type = models.IntegerField('Type', primary_key=True)
    nom = models.CharField('Nom', max_length=20)
    details = models.TextField('Details', max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'type_reparition'

    def __str__(self):
        return self.nom


class Voiture(models.Model):
    matricule = models.CharField('Matricule', primary_key=True, max_length=10)
    marque = models.CharField('Marque', max_length=20)
    type = models.CharField('Type', max_length=20)
    date_fabrication = models.DateField('Date de fabrication')
    kilometrage = models.IntegerField('Kilométrage', blank=True, null=True)
    date_arrivee = models.DateField("Date d'arrivée")

    class Meta:
        managed = False
        db_table = 'voiture'
    
    def __str__(self):
        return 'Voiture {} de matricule {}'.format(self.marque ,self.matricule)
