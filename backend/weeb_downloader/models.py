import uuid
from django.db import models

# Create your models here.


class Anime (models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=255, unique=True)
    episode_count = models.IntegerField(default=0)
    anime_url = models.URLField(unique=True)
