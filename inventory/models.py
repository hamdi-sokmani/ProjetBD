from django.db import models
# Create your models here.

class type_voiture(models.Model):
    nom_type_voiture=models.CharField("Type de voiture", max_length=50)

    def __str__(self):
        return self.nom_type_voiture


class modele(models.Model):
    
    nom_modele=models.CharField("Nom du modèle", max_length=50)
    id_type_voiture=models.ForeignKey(type_voiture, verbose_name = "Type de voiture", on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_modele


class client(models.Model):
    
    nom_client=models.CharField("Nom", max_length=50)
    prenom_client=models.CharField("Prénom", max_length=50)
    mail=models.EmailField("Email")
    numtel=models.CharField("Numéro du téléphone", max_length=50)
    address=models.CharField("Address", max_length=150)

    def __str__(self):
        return '{} {}'.format(self.nom_client, self.prenom_client)


class voiture(models.Model):
    
    matricule=models.CharField("Matricule", max_length=10)
    date_fabrication=models.DateField("Date de fabrication")
    id_modele=models.ForeignKey(modele, verbose_name = "Modèle de la voiture",  on_delete=models.CASCADE)
    id_client=models.ForeignKey(client, verbose_name = "Client",  on_delete=models.CASCADE)

    def __str__(self):
        return '{} de {}'.format(self.id_modele, self.id_client)


class poste(models.Model):
    
    nom_poste=models.CharField("Nom du poste", max_length=50)

    def __str__(self):
        return self.nom_poste

    
class employe(models.Model):
    
    nom_employe=models.CharField("Nom", max_length=50)
    prenom_employe=models.CharField("Prénom", max_length=150)
    date_debut=models.DateField("Date du début du travail")
    date_fin=models.DateField("Date de fin du travail")
    estActive=models.BooleanField("Actuellement employé")
    id_poste=models.ForeignKey(poste, verbose_name = "Poste du l'employé", on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.nom_employe, self.prenom_employe)

    
class horaire(models.Model):
    
    temps_de=models.CharField("Début du service", max_length=50)
    temps_a=models.CharField("Fin du service", max_length=50)
    date_horaire=models.DateField("Date du service")
    id_employe=models.ForeignKey(employe, verbose_name = "Employé", on_delete=models.CASCADE)
    id_poste=models.ForeignKey(poste, verbose_name = "Poste", on_delete=models.CASCADE)

    def __str__(self):
        return "Horaire de {} de poste {}".format(self.id_employe, self.id_poste)


class service(models.Model):
    
    nom_service=models.CharField("Nom du service", max_length=50)
    detail_service=models.CharField("Description", max_length=250)

    def __str__(self):
        return self.nom_service

        
class visite(models.Model):
    
    visite_date=models.DateField("Date de visite")
    matricule=models.CharField("Matricule", max_length=10)
    visite_prix=models.CharField("Prix à payer", max_length=10)
    id_client=models.ForeignKey(client, verbose_name = "Client", on_delete=models.CASCADE)
    id_voiture=models.ForeignKey(voiture, verbose_name = "Voiture", on_delete=models.CASCADE)
    id_service=models.ForeignKey(service, verbose_name = "Service", on_delete=models.CASCADE)

    def __str__(self):
        return "Visite de {} de voiture {} pour {}".format(self.id_client, self.id_voiture, self.id_service)
    