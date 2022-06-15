
from rest_framework import serializers
from app_api.models.markers import Marker

class MarkerSerializer(serializers.ModelSerializer):
    """JSON serializer for markers
    """
    class Meta:
        model = Marker
        fields = ('id', 'year_erected', 'marker_name', 'marker_text', 'civil_war_site', 'notes', 'location', 'latitude', 'longitude', 'condition', 'mapped_location', 'images', 'tags')
        depth = 1