from django.db import models


# Create your models here.
class AcademicInfo(models.Model):
    idUser = models.CharField(max_length=255)

class TermSummary(models.Model):
    academicDegree = models.CharField(max_length=255)
    program = models.CharField(max_length=255)
    term = models.CharField(max_length=255)
    termAverage = models.FloatField()
    average = models.FloatField()
    approvedCredits = models.IntegerField()
    semester = models.IntegerField()
    academicSituation = models.CharField(max_length=255)
    academic_info = models.ForeignKey(AcademicInfo, on_delete=models.CASCADE)

class Classes(models.Model):
    term = models.CharField(max_length=255)
    classId = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    grade = models.FloatField()
    academic_info = models.ForeignKey(AcademicInfo, on_delete=models.CASCADE)

class BasicInfo(models.Model):
    idUser = models.CharField(max_length=255)
    countryOfBirth = models.CharField(max_length=255)
    stateOfBirth = models.CharField(max_length=255)
    birthDate = models.CharField(max_length=255)
    maritalStatus = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    livesWith = models.CharField(max_length=255)
    works = models.BooleanField()
    schoolCity = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=255)

class LibraryHistory(models.Model):
    idUser = models.CharField(max_length=255)

class TransactionLibrary(models.Model):
    idResource = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    library_history = models.ForeignKey(LibraryHistory, on_delete=models.CASCADE)