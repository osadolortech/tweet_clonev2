from django.contrib import admin
from .models import ProfileModel,TweetModel,RetweetModel,CommentModel,LikeModel

admin.site.register((ProfileModel,TweetModel,RetweetModel,CommentModel,LikeModel,))

# Register your models here.
