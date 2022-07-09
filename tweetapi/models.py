from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfileModel(models.Model):
    first_name = models.CharField(max_length=120,blank=True)
    last_name = models.CharField(max_length=120,blank=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    bio = models.CharField(max_length=150)
    location = models.CharField(max_length=60)
    birth_date = models.DateField(editable=True)


class TweetModel(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name='tweet')
    content = models.TextField(max_length=160,blank=True)
    created_date = models.TimeField(auto_now=True)

    def __str__(self):
        return self.content



class CommentModel(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name="comment")
    tweet = models.ForeignKey(TweetModel,related_name="comment",on_delete=models.CASCADE)
    content = models.CharField(max_length=160)
    created_date = models.DateTimeField(auto_now=True)

class LikeModel(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="like")
    tweet = models.ForeignKey(TweetModel,on_delete=models.CASCADE,related_name="like")
    created_date = models.DateTimeField(auto_now_add=True)


class RetweetModel(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="retweet")
    tweet = models.ForeignKey(TweetModel,on_delete=models.CASCADE,related_name="retweet")
    created_date= models.DateTimeField(auto_now_add=True)
    
