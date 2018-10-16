from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.



class Chore(models.Model):
    task = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    points = models.IntegerField()

    def __str__(self):
        return self.task


class Child(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    chores = models.ManyToManyField(Chore)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()