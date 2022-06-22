from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.models import Tag
from app_api.serializers import TagSerializer

class TagView(ViewSet):
    """Unforgotten Nashville tag views"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single tag
            Returns:
            Response -- JSON serialized tag
        """
        try:
            tags = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tags)
            return Response(serializer.data)
        except Tag.DoesNotExist as ex:
            return Response({'message' : ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all tags
        Returns:
            Response -- JSON serialized list of tags
        """
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)