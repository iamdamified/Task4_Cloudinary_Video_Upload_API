from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=100)
    video = CloudinaryField(resource_type='video')
    duration = models.FloatField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
