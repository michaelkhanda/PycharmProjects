from django.db import models


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)


class Album(models.Model):
    name = models.CharField(max_length=100)
    release_year = models.IntegerField()
    artists = models.ManyToManyField(Artist)


class Song(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
