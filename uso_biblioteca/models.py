from django.db import models


# Create your models here.

#Uso y Recursos biblioteca
class LibUse(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    idUser = models.CharField(max_length=255)


class TranLib(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    idResource = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    libUse = models.ForeignKey(LibUse, on_delete=models.CASCADE)

class LibRes(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    idResource = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    dateCreated = models.CharField(max_length=255)
    copies = models.IntegerField()
    typeRes = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)


#Uso y Recursos AZ
class AzUse(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    idUser = models.CharField(max_length=255)


class TranAz(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    idResource = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    typeUse = models.CharField(max_length=255)
    azUse = models.ForeignKey(AzUse, on_delete=models.CASCADE)

class AzRes(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    idResource = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    dateCreated = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    repo = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)


#Uso y Recursos Repositorio Institucional
class RepoUse(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    idUser = models.CharField(max_length=255)


class TranRepo(models.Model):
    idResource = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    repoUse = models.ForeignKey(RepoUse, on_delete=models.CASCADE)

class RepoRes(models.Model):
    idResource = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    dateCreated = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    program = models.CharField(max_length=255)
    repo = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
