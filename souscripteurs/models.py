from django.db import models


class Assureurs(models.Model):
    nom = models.CharField(max_length=100)
    adresseMail = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.nom


class Souscripteurs(models.Model):
    nom = models.CharField(max_length=100)
    dateEffet = models.DateField()
    dateEcheance = models.DateField()
    assureur = models.ForeignKey(Assureurs, on_delete=models.CASCADE)
    territorialite = models.CharField(max_length=100)
    consultationGeneraliste = models.IntegerField()
    consultationSpecialiste = models.IntegerField()
    pharmacie = models.IntegerField()
    vitamines = models.IntegerField()
    vaccins = models.IntegerField()
    hospitalisation = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.nom


