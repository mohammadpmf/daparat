from django.db import models
from django.contrib.auth import get_user_model


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)