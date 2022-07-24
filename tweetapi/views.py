from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Q
from .models import TweetModel,ProfileModel,CommentModel,LikeModel,RetweetModel
from django.contrib.auth.models import User
from .registration import RegistrationSerializer
from .permissions import TwitterUserPermission
from .serializer import ProfileSerilizer,TweetSerializer,CommentSerializer,RetweetSerializer,LikeSerializer,UserSerializer
# Create your views here.

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerilizer

class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [TwitterUserPermission]
    queryset = ProfileModel.objects.all()
    serializer_class = ProfileSerilizer

class TweetView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = TweetModel.objects.all()
    serializer_class = TweetSerializer

class TweetViewDetails(generics.RetrieveDestroyAPIView):
    queryset = TweetModel.objects.all()
    serializer_class= TweetSerializer

class CommentView(generics.ListCreateAPIView):
    permission_classes = [TwitterUserPermission]
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

class CommentDetails(generics.RetrieveDestroyAPIView):
    permission_classes = [TwitterUserPermission]
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

class LikeView(generics.ListCreateAPIView):
    permission_classes = [TwitterUserPermission]
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
    permission_classes = [TwitterUserPermission]
    queryset = RetweetModel.objects.all()
    serializer_class = RetweetSerializer

    def perform_create(self, serializer):
        queryset = self.filter_queryset(self.get_queryset())
        subset = queryset.filter(Q(owner_id=self.request.data['owner']) & Q(tweet_id=self.request.data['tweet']))
        if subset.count() > 0:
            subset.first().delete()
            return
        serializer.save()
    
class RetristrationView(generics.CreateAPIView):
    permission_classes=[AllowAny]
    authentication_classes=[]
    serializer_class = RegistrationSerializer
    def post(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        user=serializers.save()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "message":"user created successfully, login to use your account"
        })