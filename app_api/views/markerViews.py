from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.models import Marker, Tag, MarkerTag, markerTags
from app_api.serializers import MarkerSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action

class MarkerView(ViewSet):
    """Unforgotten Nashville marker views"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single marker
            Returns:
            Response -- JSON serialized marker
        """
        try:
            markers = Marker.objects.get(pk=pk)
            serializer = MarkerSerializer(markers)
            return Response(serializer.data)
        except Marker.DoesNotExist as ex:
            return Response({'message' : ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all markers
        Returns:
            Response -- JSON serialized list of markers
        """
        markers = Marker.objects.all()
        serializer = MarkerSerializer(markers, many=True)
        return Response(serializer.data)
    
    @action(methods=['put'], detail=True)
    def add_tag(self, request, pk):
        """Post request for a user to assign a tag to a marker"""
        tag = Tag.objects.get(pk=request.data["tag"])
        user = User.objects.get(pk=request.auth.user.id)
        MarkerTag.objects.create(marker_id=pk, user=user, tag=tag)
        return Response({'message': 'Tag added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def remove_tag(self, request, pk):
        """Post request for a user to remove a tag from a marker"""
        tag = Tag.objects.get(pk=pk)
        user = User.objects.get(pk=request.auth.user.id)
        markerTag = MarkerTag.objects.get(marker_id=pk, user=user, tag=tag)
        markerTag.delete()
        return Response({'message': 'Tag removed'}, status=status.HTTP_201_CREATED)
    
