from django.db import models


class Post(models.Model):
    text = models.TextField(blank=True, null=True)


class Tag(models.Model):
    tag = models.CharField(max_length=150, unique=True)
    post = models.ManyToManyField(Post)
