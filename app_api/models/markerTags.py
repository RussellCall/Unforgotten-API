from django.db import models
from app_api.models import Marker
from app_api.models.tags import Tag
from django.contrib.auth.models import User

class MarkerTag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    marker = models.ForeignKey(Marker, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
