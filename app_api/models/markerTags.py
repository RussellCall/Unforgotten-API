from django.db import models
from .markers import Marker
from .tags import Tag

class MarkerTag(models.Model):
    marker = models.ForeignKey(Marker, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
