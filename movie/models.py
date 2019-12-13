from django.db import models
from category.models import Category


class Movie(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    note = models.FloatField()
    date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title