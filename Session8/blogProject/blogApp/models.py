from django.db import models
import datetime
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.title
# Create your models here.
