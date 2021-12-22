from django.db import models

# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    passward = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    movie1 = models.CharField(max_length=100, null=True, blank=True)
    movie2 = models.CharField(max_length=100, null=True, blank=True)
    movie3 = models.CharField(max_length=100, null=True, blank=True)
    movie1_img = models.ImageField(null=True, blank=True)
    movie2_img = models.ImageField(null=True, blank=True)
    movie3_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.username

