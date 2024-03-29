from django.db import models

class Trains(models.Model) :
    trainID = models.AutoField(primary_key=True)
    type = models.CharField(max_length = 30)
    n = models.IntegerField()
    heure = models.CharField(max_length = 5)
    destination = models.CharField(max_length = 30)
    voie = models.IntegerField()