from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfileModel(models.Model):
    owner = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    bio = models.CharField(max_length=150,null=True)
    location = models.CharField(max_length=60, null=True)
    birth_date = models.DateField(editable=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner

class TweetModel(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name='tweet')
    content = models.TextField(max_length=160)
    created_date = models.TimeField(auto_now=True)

    # def get_first_name(self):
    #     return self.name.first_name

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.content

    @property
    def number_of_likes(self):
        return LikeModel.objects.filter(tweet=self).count()

    @property
    def number_of_retweets(self):
        return RetweetModel.objects.filter(tweet=self).count()


class CommentModel(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name="comments")
    tweet = models.ForeignKey(TweetModel,on_delete=models.CASCADE,related_name="comments")
    content = models.CharField(max_length=160)
    created_date = models.DateTimeField(auto_now=True)

class LikeModel(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="likes")
    tweet = models.ForeignKey(TweetModel,on_delete=models.CASCADE,related_name="likes")
    created_date = models.DateTimeField(auto_now_add=True)


class RetweetModel(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="retweets")
    tweet = models.ForeignKey(TweetModel,on_delete=models.CASCADE,related_name="retweets")
    created_date= models.DateTimeField(auto_now_add=True)
    
