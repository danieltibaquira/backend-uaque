from django.db import models


# Modelo mediante el cual se almacena la información básica de los estudiantes
class InfoBasica(models.Model):
    idUser = models.CharField(max_length=255)
    countryOfBirth = models.CharField(max_length=255)
    stateOfBirth = models.CharField(max_length=255)
    birthDate = models.CharField(max_length=255)
    maritalStatus = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    livesWith = models.CharField(max_length=255)
    works = models.BooleanField()
    schoolCity = models.CharField(max_length=255)
    age = models.IntegerField(max_length=2)
    gender = models.CharField(max_length=255)


