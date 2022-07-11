from unicodedata import name
from django.urls import path
from .views import ProfileView,ProfileDetails,TweetView,TweetViewDetails,CommentView,CommentDetails,LikeView,UserView,RetweetView

urlpatterns=[

    path("user", UserView.as_view(), name="create_user"),
    path("profile", ProfileView.as_view(), name="profile"),
    path("profile/<int:pk>",ProfileDetails.as_view(), name="profile_details"),
    path("tweet",TweetView.as_view(), name="tweet_view"),
    path("tweet/<int:Pk>", TweetViewDetails.as_view(), name="delete_tweet"),
    path("comment",CommentView.as_view(), name="create_comment"),
    path("comment/<int:pk>", CommentDetails.as_view(), name="delete_comment"),
    path("like", LikeView.as_view(), name="like"),
    path("retweet", RetweetView.as_view(), name="retweet"),

]