from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    datetime_created = models.DateTimeField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.description[:40]}"