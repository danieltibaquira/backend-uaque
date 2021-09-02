from django.db import models


# Create your models here.
class UbicacionRed(models.Model):
    idUser = models.CharField(max_length=255)
    location = models.CharField(max_length=255)


