from django.db import models

class Newuser(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=8)
# Create your models here.
