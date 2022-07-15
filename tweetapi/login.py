from django.conf import settings
import jwt
from .serializer import UserSerializer
from .registration import UserloginSerializer
from rest_framework.generics import CreateAPIView
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings



class Login(CreateAPIView):
    serializer_class = UserloginSerializer
    def post(self, request,format=None):
        serializer = UserloginSerializer(data=request.data)
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
                    "iat":datetime.datetime.utcnow()
                }
                access_token = jwt.encode(payload,"secret",algorithm="HS256")
                refresh_token = jwt.encode(payload2,"secret",algorithm="HS256")
                response = Response()
                response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)
                response.data = {
                    "username":username,
                    'token':access_token
                }
                return response
            else:
                error = {"Error": status.HTTP_400_BAD_REQUEST,"error_message":"Invalid Username or password"}
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            


class UserApiView(APIView):
    def get(self,request):
        token = request.COOKIES.get('refreshToken')
        if not token:
            return Response({"error": "Authentication failed" }, status=status.HTTP_400_BAD_REQUEST)
        try:
            payload = jwt.decode(token, "secret", algorithms="HS256")
        except jwt.ExpiredSignatureError:
            return Response({"error": "Authentication failed" }, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(id=payload['id']).first()
        serializer=UserSerializer(user)
        return Response(serializer.data)

class Logout(APIView):
    def get(self,request):
        logout(request)
        response = Response()
        response.delete_cookie(key="refreshToken")
        response.data={
            "message": "successfully logged out"
        }
        return response

class ChangePassword(APIView):
   pass


