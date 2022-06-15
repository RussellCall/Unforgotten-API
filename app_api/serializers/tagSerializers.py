from rest_framework import serializers
from app_api.models import Tag

class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for markers
    """
    class Meta:
        model = Tag
        fields = ('id', 'label')
        depth = 1