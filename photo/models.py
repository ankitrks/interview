from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

class DateTimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add = True, blank = False, null = False)
    updated_at = models.DateTimeField(auto_now = True, blank = False, null = False)
    is_active = models.BooleanField(default = True)
    
    class Meta:
        abstract = True

class Photo(DateTimeStamp):
    title = models.CharField(max_length = 255, blank = False, null = False)
    image_file = models.URLField(max_length = 255, blank = False, null = False)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank = False, null = False, on_delete = models.CASCADE)

    def __str__(self):
        return self.title


class Album(DateTimeStamp):
    title = models.CharField(max_length = 255, blank = False, null = False)
    images = models.ManyToManyField(Photo, blank = True, null = True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank = False, null = False, on_delete = models.CASCADE)

    def __str__(self):
        return self.title