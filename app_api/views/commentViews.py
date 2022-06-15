from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.models import Comments, Marker
from app_api.serializers import CommentSerializer
from django.contrib.auth.models import User

class CommentView(ViewSet):
    """Unforgotten Nashville marker views"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single comment
            Returns:
            Response -- JSON serialized comment
        """
        try:
            comment = Comments.objects.get(pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        except Comments.DoesNotExist as ex:
            return Response({'message' : ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all comments
        Returns:
            Response -- JSON serialized list of comments
        """
        comment = Comments.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized comment instance
        """
        user = User.objects.get(pk=request.auth.user.id)
        marker = Marker.objects.get(pk=request.data["marker"])
        
        comment = Comments.objects.create(
            user=user,
            marker=marker,
            text=request.data["text"],
            )
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a comment
        Returns:
            Response -- Empty body with 204 status code
        """
        comment = Comments.objects.get(pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        comment = Comments.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)