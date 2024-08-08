from django.db import models

class Usergames(models.Model):
    name = models.CharField(max_length=255)
    games = models.CharField(max_length=255)
# Create your models here.
