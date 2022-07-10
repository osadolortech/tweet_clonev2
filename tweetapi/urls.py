from unicodedata import name
from django.urls import path
from .views import ProfileView,ProfileDetails,TweetView

urlpatterns=[
    path("profile", ProfileView.as_view(), name="profile"),
    path("profile/<int:pk>",ProfileDetails.as_view(), name="profile_details"),
    path("tweet",TweetView.as_view(), name="tweet_view")
]