from asyncore import write
from rest_framework import serializers
from .models import ProfileModel, TweetModel,LikeModel,RetweetModel,CommentModel
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = (
            "id","owner","bio","location","birth_date"
        )

class UserSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer()
    tweet  = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    retweets = serializers.PrimaryKeyRelatedField(many=True,read_only= True)
    class Meta:
        model = User
        fields = (
            "id","tweet","comments","retweets","likes","first_name","last_name","user_profile","username"
        )


class TweetSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    retweets = serializers.PrimaryKeyRelatedField(many=True,read_only= True)
    owner= serializers.ReadOnlyField(read_only=True, source='owner.username')
    name = serializers.ReadOnlyField(read_only=True, source='owner.first_name')
    class Meta:
        model = TweetModel
        fields = (
            "id","name","owner","content","created_date","comments","likes","retweets","number_of_likes","number_of_retweets"
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
