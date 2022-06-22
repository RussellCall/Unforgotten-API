from rest_framework import serializers
from app_api.models import Image

class ImageSerializer(serializers.ModelSerializer):
    """JSON serializer for markers
    """
    class Meta:
        model = Image
        fields = ('id', 'image', 'user', 'marker')
        depth = 2