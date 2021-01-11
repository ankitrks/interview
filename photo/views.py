from rest_framework.viewsets import ModelViewSet

from django.shortcuts import render

from photo.models import *
from photo.serializers import PhotoSerializer, AlbumSerializer

class PhotosViewSet(ModelViewSet):
    queryset = Photo.objects.all() # can be overwritten by get_queryset method
    serializer_class = PhotoSerializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.filter(is_active=True) # can be overwritten by get_queryset method
    serializer_class = AlbumSerializer
