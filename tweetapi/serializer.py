from rest_framework import serializers
from .models import ProfileModel, TweetModel,LikeModel,RetweetModel,CommentModel
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    tweet  = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    retweets = serializers.PrimaryKeyRelatedField(many=True,read_only= True)
    password = serializers.CharField(required=True,write_only=True)
    class Meta:
        model = User
        fields = (
            "id","username","password","tweet","comments","retweets","likes"
        )
       

class ProfileSerilizer(serializers.ModelSerializer):
    class Meta:

        model = ProfileModel
        fields = (
            "id","owner","first_name","last_name","bio","location","birth_date"
        )

class TweetSerializer(serializers.ModelSerializer):

    comments = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    retweets = serializers.PrimaryKeyRelatedField(many=True,read_only= True)
    class Meta:
        model = TweetModel
        fields = (
            "id","owner","content","created_date","comments","likes","retweets","number_of_likes","number_of_retweets"
        )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields =(
            "id","owner","tweet","content","created_date"
        )

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeModel
        fields = (
            "id","owner","tweet","created_date"
        )

class RetweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetweetModel
        fields = (
            "id","owner","tweet","created_date"
        )
