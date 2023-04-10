from django.db import models
import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    deadline = models.DateTimeField(null=True, default="")

    def __str__(self):
        return self.title