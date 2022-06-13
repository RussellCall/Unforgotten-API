from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.models import Marker
from app_api.serializers import MarkerSerializer

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
        """Handle GET requests to get all game types
        Returns:
            Response -- JSON serialized list of game types
        """
        markers = Marker.objects.all()
        serializer = MarkerSerializer(markers, many=True)
        return Response(serializer.data)