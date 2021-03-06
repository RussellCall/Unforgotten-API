from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from app_api.models import Comments, Marker
from app_api.serializers import CommentSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action


class CommentView(ViewSet):
    """Unforgotten Nashville marker views"""
    
    def retrieve(self, request, pk):  # get a comment by id
        """Handle GET requests for single comment
            Returns:
            Response -- JSON serialized comment
        """
        try:
            comment = Comments.objects.get(pk=pk) # get comment by id
            serializer = CommentSerializer(comment) # serialize comment
            return Response(serializer.data)
        except Comments.DoesNotExist as ex: 
            return Response({'message' : ex.args[0]}, status=status.HTTP_404_NOT_FOUND) # return error message if comment does not exist
        
    def list(self, request): # get all comments
        """Handle GET requests to get all comments
        Returns:
            Response -- JSON serialized list of comments
        """
        comment = Comments.objects.all()
        marker_id = request.query_params.get('marker_id', None) # get marker_id from query params
        if marker_id is not None: 
                marker = marker_id.filter(marker_id=marker)  
        serializer = CommentSerializer(comment, many=True) 
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized comment instance
        """
        user = User.objects.get(pk=request.auth.user.id)
        marker_id = Marker.objects.get(pk=request.data["marker_id"])
        
        comment = Comments.objects.create(
            user=user,
            marker=marker_id,
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
    
    
    @action(methods=['get'], detail=True)
    def comments_by_marker(self, request, pk):
        comments = Comments.objects.filter(marker=pk)
        serializer=CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
