from rest_framework import serializers
from todos import models


class TodoSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format="hex")

    class Meta:
        model = models.Todo
        fields = (
            "id",
            "name",
            "color",
            "done",
        )
