from django.urls import path
from .views import CreateProfile,UpdateProfileDetails,RetreiveUserView,TweetView,TweetViewDetails,CommentView,CommentDetails,LikeView,RetweetView,RegistrationView
from .login import Login,Logout,ProfileView,ChangePassword,Resetpassword,UserPasswordReset
urlpatterns=[

    # path("user", UserView.as_view(), name="create-user"),
    path("user/<int:pk>", RetreiveUserView.as_view(), name="get-user"),
    path("create-profile", CreateProfile.as_view(), name="profile"),
    path("edith-profile/<int:owner>",UpdateProfileDetails.as_view(), name="profile-details"),
    path("tweet",TweetView.as_view(), name="tweet_view"),
    path("tweet/<int:pk>", TweetViewDetails.as_view(), name="delete-tweet"),
    path("comment",CommentView.as_view(), name="create-comment"),
    path("comment/<int:pk>", CommentDetails.as_view(), name="delete-comment"),
    path("like", LikeView.as_view(), name="like"),
    path("retweet", RetweetView.as_view(), name="retweet"),
    path("register", RegistrationView.as_view(),name="register"),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('profile', ProfileView.as_view(), name='userview'),
    path('change-password', ChangePassword.as_view(), name='change-password'),
    path('send-resetlink', Resetpassword.as_view(), name='reset-password'),
    path('reset-password/<uid>/<token>',UserPasswordReset.as_view())

]