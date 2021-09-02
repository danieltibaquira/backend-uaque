from django.db import models


# Create your models here.
class InfoAcademica(models.Model):
    idUser = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    program = models.CharField(max_length=255)

class Schedule(models.Model):
    # idClass = models.CharField(max_length=255)
    term = models.CharField(max_length=255)
    academicLevel = models.CharField(max_length=255)
    idProfessor = models.CharField(max_length=255)
    info_acad = models.ForeignKey(InfoAcademica, on_delete=models.CASCADE)


class AcademicGroup(models.Model):
    # idGroup = models.CharField(max_length=255)
    idDirector = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    info_acad = models.ForeignKey(InfoAcademica, on_delete=models.CASCADE)


class RecreativeActivity(models.Model):
    # idActivity = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    info_acad = models.ForeignKey(InfoAcademica, on_delete=models.CASCADE)


