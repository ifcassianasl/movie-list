from django.db import models
from library.models import Library
import uuid


class Category(models.Model):
    kind = models.CharField(max_length=64)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.kind