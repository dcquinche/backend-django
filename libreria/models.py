from django.db import models

# Create your models here.
class Libreria(models.Model):
    name = models.CharField(max_length=100)
    isActive = models.BooleanField()
    isUsed = models.BooleanField()
