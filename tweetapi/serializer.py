from rest_framework import serializers
from .models import ProfileModel, TweetModel


class ProfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = (
            "id","username","first_name","last_name","bio","location","birth_date"
        )


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetModel
        fields = (
            "id","owner","content","created_date"
        )