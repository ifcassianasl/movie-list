from django.db import models
from django.contrib.auth.models import User
import uuid


class Library(models.Model):
    title = models.CharField(max_length=64)
    details = models.CharField(max_length=250)
    users = models.ManyToManyField(User)

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
