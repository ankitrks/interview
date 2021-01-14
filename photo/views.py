from rest_framework.viewsets import ModelViewSet

from django.shortcuts import render

from photo.models import *
from photo.serializers import PhotoSerializer, AlbumSerializer

class PhotosViewSet(ModelViewSet):
    queryset = Photo.objects.filter(is_active=True)
    serializer_class = PhotoSerializer

    def get_queryset(self):
    	return self.queryset.filter(uploaded_by = self.request.user)

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.filter(is_active=True)
    serializer_class = AlbumSerializer

    def get_queryset(self):
    	return self.queryset.filter(uploaded_by = self.request.user)
