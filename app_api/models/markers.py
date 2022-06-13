from django.db import models

class Marker(models.Model):
    year_erected = models.DateField()
    marker_name = models.CharField(max_length=55)
    marker_text = models.CharField(max_length=12)
    civil_war_site = models.BooleanField()
    notes = models.CharField(max_length=500)
    location = models.CharField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    condition = models.CharField(max_length=55)
    mapped_location = models.CharField(max_length=55)
