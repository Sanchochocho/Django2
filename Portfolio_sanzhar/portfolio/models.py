from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 100, unique = True)
    published_date = models.DateField()
    pages = models.IntegerField(default=0, null=False)
    description = models.TextField(blank=True)