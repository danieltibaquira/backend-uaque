from djongo import models
# from django.contrib.postgres.fields import ArrayField

# class Group(models.Model):
#     themes = ArrayField(models.CharField(max_length=255, blank=True))
#     members = ArrayField(models.CharField(max_length=255, blank=True))

# class Feedback(models.Model):
#     groupId = models.CharField(max_length=255)

class Recomemendation(models.Model):
    itemId = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    userId = models.CharField(max_length=255)
    dewey = models.CharField(max_length=255)
    themes = models.CharField(max_length=255)
    # score = models.FloatField()
    # feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
