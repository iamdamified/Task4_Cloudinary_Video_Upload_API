from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from .models import Video
from .serializers import VideoSerializer
import cloudinary

# import tempfile
# import requests
# Create your views here.

class CreateVideo(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
