from django.db import models
from django.contrib.auth.models import User
from app_api.models.markers import Marker


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    marker = models.ForeignKey(Marker, on_delete=models.CASCADE)
    text = models.TextField()