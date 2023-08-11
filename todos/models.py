import uuid
from django.db import models


class Todo(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    name = models.CharField(max_length=200)
    # description = models.TextField()
    color = models.CharField(max_length=20)
    done = models.BooleanField()

    def __str__(self):
        return self.name
