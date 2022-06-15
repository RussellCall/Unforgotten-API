from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.models import Image
from app_api.serializers import ImageSerializer

class ImageView(ViewSet):
    """Unforgotten Nashville views"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single image
            Returns:
            Response -- JSON serialized image
        """
        try:
            images = Image.objects.get(pk=pk)
            serializer = ImageSerializer(images)
            return Response(serializer.data)
        except Image.DoesNotExist as ex:
            return Response({'message' : ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all images
        Returns:
            Response -- JSON serialized list of images
        """
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)