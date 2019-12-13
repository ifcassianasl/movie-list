from django.db import models
from category.models import Category
import uuid


class Movie(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    note = models.FloatField()
    date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
