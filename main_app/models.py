from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chore(models.Model):
    task = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    points = models.IntegerField()

    def __str__(self):
        return self.task