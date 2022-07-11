from rest_framework import generics
from django.db.models import Q
from .models import TweetModel,ProfileModel,CommentModel,LikeModel,RetweetModel
from django.contrib.auth.models import User
from .serializer import ProfileSerilizer,TweetSerializer,CommentSerializer,RetweetSerializer,LikeSerializer,UserSerializer

# Create your views here.

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileView(generics.ListCreateAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerilizer

class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerilizer

class TweetView(generics.ListCreateAPIView):
    queryset = TweetModel.objects.all()
    serializer_class = TweetSerializer

class TweetViewDetails(generics.RetrieveDestroyAPIView):
    queryset = TweetModel.objects.all()
    serializer_class= TweetSerializer

class CommentView(generics.ListCreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = TweetSerializer

class CommentDetails(generics.RetrieveDestroyAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

class LikeView(generics.ListCreateAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        queryset = self.filter_queryset(self.get_queryset())
        subset = queryset.filter(Q(owner_id=self.request.data['owner']) & Q(tweet_id=self.request.data['tweet']))
        if subset.count() > 0:
            subset.first().delete()
            return
        serializer.save()

class RetweetView(generics.ListCreateAPIView):
    queryset = RetweetModel.objects.all()
    serializer_class = RetweetSerializer

    def perform_create(self, serializer):
        queryset = self.filter_queryset(self.get_queryset())
        subset = queryset.filter(Q(owner_id=self.request.data['owner']) & Q(tweet_id=self.request.data['tweet']))
        if subset.count() > 0:
            subset.first().delete()
            return
        serializer.save()
    