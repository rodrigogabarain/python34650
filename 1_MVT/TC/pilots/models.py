from django.db import models

# Create your models here.
class Pilots(models.Model):
    name = models.CharField(max_length=100)
    points = models.FloatField()
    enabled = models.BooleanField()
