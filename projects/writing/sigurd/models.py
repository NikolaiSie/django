from django.db import models

# Create your models here.
class Haiku(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=400, null=True)
    line_1 = models.CharField(max_length=100, null=True)
    line_2 = models.CharField(max_length=100, null=True)
    line_3 = models.CharField(max_length=100, null=True)


class Chapter(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()


class Poem(models.Model):
    title = models.CharField(max_length=200, null=True)
    text = models.TextField(null=True)

class Story(models.Model):
    title = models.CharField(max_length=200, null=True)
    text = models.TextField(null=True)