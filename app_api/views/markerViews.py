from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models import Marker

class MarkerView(ViewSet):
    """Unforgotten Nashville marker views"""
    
    def retrieve(self, request, pk):
                """Handle GET requests for single event
            Returns:
            Response -- JSON serialized event
        """
        try:
            marker = Marker.objects.get(pk=pk)
            serializer = 