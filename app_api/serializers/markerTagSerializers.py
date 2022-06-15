from rest_framework import serializers
from app_api.models import MarkerTag

class MarkerTagSerializer(serializers.ModelSerializer):
    """JSON serializer for markers
    """
    class Meta:
        model = MarkerTag
        fields = ('id', 'marker', 'tag')
        depth = 1