from rest_framework import serializers
from app_api.models import Comments

class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for markers
    """
    class Meta:
        model = Comments
        fields = ('id', 'user', 'marker', 'text')
        depth = 2