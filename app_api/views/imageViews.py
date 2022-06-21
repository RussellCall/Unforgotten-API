from urllib import request
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.models import Image
from app_api.models import Marker
from app_api.serializers import ImageSerializer
from django.contrib.auth.models import User

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
    
    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized comment instance
        """
        user = User.objects.get(pk=request.auth.user.id)
        marker_id = Marker.objects.get(pk=request.data["marker_id"])
        
        image = Image.objects.create(
            user=user,
            marker=marker_id,
            image=request.data["image"],
            )
        serializer = ImageSerializer(image)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        image = Image.objects.get(pk=pk)
        image.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)