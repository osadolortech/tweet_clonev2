from rest_framework import generics
from .models import TweetModel,ProfileModel,CommentModel,LikeModel,RetweetModel
from django.contrib.auth.models import User
from .serializer import ProfileSerilizer,TweetSerializer,CommentSerializer,RetweetSerializer,LikeSerializer

# Create your views here.

class ProfileView(generics.ListCreateAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerilizer

class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerilizer

class TweetView(generics.ListCreateAPIView):
    queryset = TweetModel.objects.all()
    serializer_class = TweetSerializer