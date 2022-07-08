from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfileModel(models.Model):
    first_name = models.CharField(max_length=120,blank=True)
    last_name = models.CharField(max_length=120,blank=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    Bio = models.CharField(max_length=150)
    Location = models.CharField(max_length=60)
    Birth_date = models.DateField(editable=True)


class TweetModel(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name='tweet')
    content = models.TextField(max_length=160,blank=True)
    created_date = models.TimeField(auto_now=True)

    def __str__(self):
        return self.content

        


