from django.db import models

# Create your models here.

class Details(models.Model):
    song_name = models.CharField(max_length=200)
    cappo = models.CharField(max_length=10)
    language = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    url = models.CharField(max_length=200)
    lyrics = models.CharField(max_length=2000)

    def __str__(self):
        return self.song_name

class Login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username + " --- " + self.password


