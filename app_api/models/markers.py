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
    
    
    # "id": 6,
    # "Year Erected": 1968,
    # "Marker Name": "Battle of Nashville Stewart's Line",
    # "Marker Text": "Loring's division of Stewart's Corps, Hood's Confederate Army of Tennessee, fought behind this stone wall Dec. 16, 1864.  All Federal attacks were beaten back until the Confederate line was broken a mile to the west.  The division retreated south through the hills toward Brentwood.",
    # "Civil War Site?": "TRUE",
    # "Notes": "",
    # "Location": "4618 Lealand Lane",
    # "Latitude": 36.086311,
    # "Longitude": -86.791167,
    # "Condition": "",
    # "Mapped Location": "POINT (-86.791167 36.086311)"