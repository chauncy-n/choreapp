from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.



class Chore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    points = models.IntegerField()
    def __str__(self):
        return self.task
    
    def get_absolute_url(self):
        return reverse('chores_detail', kwargs={'chore_id': self.id})


class Child(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    chores = models.ManyToManyField(Chore, verbose_name='Add a chore')


class Reward(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    points = models.IntegerField()
    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('rewards_detail', kwargs={'reward_id': self.id})



