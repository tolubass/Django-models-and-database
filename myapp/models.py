from django.db import models

# Create your models here.

class Books(models.Model):
    objects = models.Manager()
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField()

class Article(models.Model):
    title =models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)