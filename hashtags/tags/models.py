from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):
    text = models.TextField(blank=True, null=True)


class Tag(models.Model):
    tag = models.CharField(max_length=150, unique=True)
    post = models.ManyToManyField(Post)

    def natural_key(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tags:post_list', kwargs={'tag': self.tag})
