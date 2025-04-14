from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    task_name = models.CharField(max_length=32, null=True, blank=True)

