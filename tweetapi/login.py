
from django.conf import settings
import jwt
from .serializer import UserSerializer
from .registration import UserloginSerializer,ChangePasswordSerializer
from rest_framework.generics import CreateAPIView
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
from rest_framework.permissions import AllowAny
from .resetpassword import SendUserPasswordReset,UserPasswordReset



class Login(CreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes= []
    serializer_class = UserloginSerializer
    def post(self, request,format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get("username")
            password = serializer.data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                payload = {
                    "id":user.id,
                    "exp":settings.ACCESS_EXP,
                    "iat":datetime.datetime.utcnow()
                }
                payload2 = {
                    "id":user.id,
                    "exp":settings.REFRESH_EXP,
                    "iat":datetime.datetime.utcnow(),
                }
                access_token = jwt.encode(payload,"secret",algorithm="HS256")
                refresh_token = jwt.encode(payload2,"secret",algorithm="HS256")
                user = User.objects.filter(id=payload['id']).first()
                serializer=UserSerializer(user)
                response = Response()
                # response(key='refreshToken', value=refresh_token, httponly=True)
                response.data = {
                    "username":username,
                    'token':access_token,
                    "refresh_token":refresh_token,
                    "user":serializer.data
                }
                return response
            else:
                error = {"Error": status.HTTP_400_BAD_REQUEST,"error_message":"Invalid Username or password"}
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            


class ProfileView(APIView):
    def get(self,request):
        user = request.user
        serializer = UserSerializer(user)
        return Response({"user":serializer.data})
        # token = request.COOKIES.get('refreshToken')
        # if not token:
        #     return Response({"error": "Authentication failed" }, status=status.HTTP_400_BAD_REQUEST)
        # try:
        #     payload = jwt.decode(token, "secret", algorithms="HS256")
        # except jwt.ExpiredSignatureError:
        #     return Response({"error": "Authentication failed" }, status=status.HTTP_400_BAD_REQUEST)
        # user = User.objects.filter(id=payload['id']).first()
        # serializer=UserSerializer(user)
        # return Response({"user":serializer.data})
    

class Logout(APIView):
    def get(self,request):
        logout(request)
        response = Response()
        response.delete_cookie(key="refreshToken")
        response.data={
            "message": "successfully logged out"
        }
        return response

class ChangePassword(CreateAPIView):
    serializer_class = ChangePasswordSerializer
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data,
        context=({"user":request.user}))
        if serializer.is_valid():
            return Response({"msg":"password changed successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Resetpassword(CreateAPIView):
    permission_classes=[AllowAny]
    authentication_classes=[]
    serializer_class = SendUserPasswordReset
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message':"password reset sent, check your mail"}, status=status.HTTP_200_OK)
    


class UserPasswordReset(CreateAPIView):
    permission_classes=[AllowAny]
    authentication_classes=[]
    serializer_class = UserPasswordReset
    def post(self, request,uid,token,format=None):
        serializer = self.get_serializer(data=request.data,
        context={'uid':uid,'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':"password reset successfully"}, status=status.HTTP_200_OK)
    


