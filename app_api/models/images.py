from django.db import models
from django.contrib.auth.models import User
from app_api.models.markers import Marker



class Image(models.Model):
    
    image = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    marker = models.ForeignKey(Marker, on_delete=models.CASCADE,related_name="images")