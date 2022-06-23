from django.db import models
from app_api.models.tags import Tag

class Marker(models.Model):
    year_erected = models.CharField(max_length=55)
    marker_name = models.CharField(max_length=500)
    marker_text = models.CharField(max_length=500)
    civil_war_site = models.BooleanField()
    notes = models.CharField(max_length=500)
    location = models.CharField(max_length=55)
    latitude = models.DecimalField(max_digits=15, decimal_places=6)
    longitude = models.DecimalField(max_digits=15, decimal_places=6)
    condition = models.CharField(max_length=55)
    mapped_location = models.CharField(max_length=55)
    tags = models.ManyToManyField("Tag", through="MarkerTag")
