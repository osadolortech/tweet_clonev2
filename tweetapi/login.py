import jwt
from .serializer import UserSerializer
from rest_framework.generics import CreateAPIView
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class Login(CreateAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error":"please fill all fields"}, status=status.HTTP_400_BAD_REQUEST)
        check_user = User.objects.filter(username=username)
        if check_user == False:
            return Response({"error":"username does not exsit"})
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            payload = {
                "id":user.id,
                "exp":datetime.timedelta(minutes=2) + datetime.datetime.utcnow(),
                "iat":datetime.datetime.utcnow()
            }
            payload2 = {
                "id":user.id,
                "exp":datetime.timedelta(days=3) + datetime.datetime.utcnow(),
                "iat":datetime.datetime.utcnow()
            }
            access_token = jwt.encode(payload,"secret",algorithm="HS256")
            refresh_token = jwt.encode(payload2,"secret",algorithm="HS256")
            response = Response()
            response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)
            response.data = {
                'token':access_token
            }
            return response
        else:
            error = {"Error": status.HTTP_400_BAD_REQUEST,"error_message":"Invalid Username or password"}
        return Response(error,status=status.HTTP_400_BAD_REQUEST)

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
        return Response("sucessfully logout")
