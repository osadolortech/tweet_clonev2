from django.urls import path
from .views import CreateEdithProfileView,UpdateProfileDetails,RetriveUserView,TweetView,TweetViewDetails,CommentView,CommentDetails,LikeView,UserView,RetweetView,RetristrationView
from .login import Login,Logout,ProfileView,ChangePassword,Resetpassword,UserPasswordReset
urlpatterns=[

    path("user", UserView.as_view(), name="create_user"),
    path("user/<int:pk>", RetriveUserView.as_view(), name="get_user"),
    path("create_profile", CreateEdithProfileView.as_view(), name="profile"),
    path("edith_profile/<int:owner>",UpdateProfileDetails.as_view(), name="profile_details"),
    path("tweet",TweetView.as_view(), name="tweet_view"),
    path("tweet/<int:pk>", TweetViewDetails.as_view(), name="delete_tweet"),
    path("comment",CommentView.as_view(), name="create_comment"),
    path("comment/<int:pk>", CommentDetails.as_view(), name="delete_comment"),
    path("like", LikeView.as_view(), name="like"),
    path("retweet", RetweetView.as_view(), name="retweet"),
    path("register", RetristrationView.as_view(),name="register"),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('profile', ProfileView.as_view(), name='userview'),
    path('changepassword', ChangePassword.as_view(), name='change-password'),
    path('send-reset-link', Resetpassword.as_view(), name='reset-password'),
    path('reset-password/<uid>/<token>',UserPasswordReset.as_view())

]