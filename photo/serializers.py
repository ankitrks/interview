from rest_framework import serializers
from django.contrib.auth.models import User
from photo.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'title', 'image_file', 'uploaded_by')

    def to_representation(self, instance):
        data = super(PhotoSerializer, self).to_representation(instance)
        data.update({ 'uploaded_by' : UserSerializer(instance.uploaded_by).data })
        return data

    def to_internal_value(self, data):
        data['uploaded_by'] = 1 # self._context.get('request').user.id
        return super(PhotoSerializer, self).to_internal_value(data)

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

    def to_representation(self, instance):
        data = super(AlbumSerializer, self).to_representation(instance)
        data.update({ 'images' : PhotoSerializer(instance.images.all(), many=True).data, \
            'uploaded_by' : UserSerializer(instance.uploaded_by).data})
        return data

    def to_internal_value(self, data):
        data['uploaded_by'] = 1 # self._context.get('request').user.id
        return super(AlbumSerializer, self).to_internal_value(data)

    def validate_images(self, value):
        if self.partial:
            value += list(self.instance.images.all())
        return value