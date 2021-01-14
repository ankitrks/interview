from rest_framework import serializers
from django.contrib.auth.models import User
from photo.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')

class PhotoSerializer(serializers.ModelSerializer):
    uploaded_by = UserSerializer(default=serializers.CurrentUserDefault())
    class Meta:
        model = Photo
        fields = ('id', 'title', 'image_file', 'uploaded_by')

class AlbumSerializer(serializers.ModelSerializer):
    uploaded_by = UserSerializer(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Album
        fields = '__all__'

    def validate_images(self, value):
        # filter images that related to current user only.
        value = list(Photo.objects.filter(uploaded_by=self._context.get('request').user, \
                id__in=[item.id for item in value]).values_list('id', flat=True))
        if self.partial:
            value += list(self.instance.images.all())
        return value