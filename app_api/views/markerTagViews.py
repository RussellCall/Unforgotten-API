from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.models import MarkerTag
from app_api.serializers import MarkerTagSerializer

class MarkerTagView(ViewSet):
    """Unforgotten Nashville marker views"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single marker
            Returns:
            Response -- JSON serialized marker
        """
        try:
            markerTags = MarkerTag.objects.get(pk=pk)
            serializer = MarkerTagSerializer(markerTags)
            return Response(serializer.data)
        except MarkerTag.DoesNotExist as ex:
            return Response({'message' : ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all game types
        Returns:
            Response -- JSON serialized list of game types
        """
        markerTags = MarkerTag.objects.all()
        serializer = MarkerTagSerializer(markerTags, many=True)
        return Response(serializer.data)