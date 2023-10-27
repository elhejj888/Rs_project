from django.db import models

class Professeur(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=80)
    tel = models.CharField(max_length=15)
    pourcentage = models.DecimalField(max_digits=5, decimal_places=2)
    date_embauche = models.DateField()
    matiere = models.CharField(max_length=70)
    niveau = models.CharField(max_length=10)


class Groupe(models.Model):
    designation = models.CharField(max_length=40)
    professors = models.ForeignKey(Professeur,on_delete=models.CASCADE)
    centre = models.CharField(max_length=20)
    

class Student(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=80)
    lycee = models.CharField(max_length=100)
    centre = models.CharField(max_length=30)
    tel = models.CharField(max_length=15)
    eligibility = models.BooleanField()
    address = models.CharField(max_length=250)
    groupe = models.ForeignKey(Groupe,on_delete=models.CASCADE)

class Utilisateur(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=80)
    tel = models.CharField(max_length=15)
    post = models.CharField(max_length=20)
    centre = models.CharField(max_length=30)





    
