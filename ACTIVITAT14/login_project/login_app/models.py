from django.db import models

class Usuari(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    ciutat = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
