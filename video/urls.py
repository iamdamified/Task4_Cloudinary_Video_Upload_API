from django.urls import path
from .views import *

urlpatterns = [
    path("video_upload/", CreateVideo.as_view(), name="upload_video")
]