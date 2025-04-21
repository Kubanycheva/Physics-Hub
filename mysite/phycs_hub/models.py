from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)
    bio = models.TextField()
    education = models.CharField(max_length=62, null=True, blank=True, verbose_name='Образование')
    achievements = models.CharField(max_length=62, null=True, blank=True, verbose_name='достижения')
    roles = models.CharField(max_length=62, null=True, blank=True)
    projects = models.CharField(max_length=72, null=True, blank=True)
    interests = models.CharField(max_length=62, null=True, blank=True)
    contacts = models.CharField(max_length=62, null=True, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    authors = models.CharField(max_length=32, null=True, blank=True)
    filepath = models.FileField(upload_to='materials/')
    source = models.URLField(blank=True)
    sourceLabel = models.TextField(null=True, blank=True)
    storagePath = models.CharField(max_length=255, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='materials', blank=True)
    
    def __str__(self):
        return self.name


class Olympiad(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    description = models.TextField()
    logo_url = models.URLField(blank=True, null=True)
    logo_storage_path = models.CharField(max_length=255, blank=True, null=True)


    cover_url = models.URLField(blank=True, null=True)
    cover_storage_path = models.CharField(max_length=255, blank=True, null=True)
    regulations_url = models.URLField(blank=True, null=True)
    regulations_storage_path = models.CharField(max_length=255, blank=True, null=True)

    registration_start = models.DateField()
    registration_end = models.DateField()
    results_date = models.DateField(blank=True, null=True)
    results_url = models.URLField(blank=True, null=True)
    participant_count = models.PositiveIntegerField(default=0)

    socialLinks = models.URLField(blank=True)
    registrationFormUrl = models.URLField(blank=True)
    organizers = models.CharField(max_length=52, null=True, blank=True)
    stages = models.CharField(max_length=52, null=True, blank=True)
    regions = models.CharField(max_length=52, null=True, blank=True)
    priority = models.CharField(max_length=72, null=True, blank=True)

    def __str__(self):
        return self.name


class Stage(models.Model):
    olympiad = models.ForeignKey(Olympiad, null=True, blank=True, on_delete=models.CASCADE, related_name='olympiad_stages')
    name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    practise_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=255)
    logo_url = models.URLField(blank=True, null=True)
    link = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    description = models.TextField()
    images = models.ImageField(upload_to='images/product', null=True, blank=True)
    imageStoragePaths = models.ImageField(upload_to='image/storage', null=True, blank=True)
    inStock = models.BooleanField(blank=True)
    sizes = models.CharField(max_length=32, null=True, blank=True)
    type = models.CharField(max_length=82, null=True, blank=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


