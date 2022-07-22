from django.forms import ValidationError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import serializers
from django.contrib.auth.models import User

class SendUserPasswordReset(serializers.Serializer):
    username = serializers.CharField(max_length=125)
    class Meta:
        fields = (
            'username'
        )
    def validate(self, attrs):
        username = attrs.get('username')
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token=PasswordResetTokenGenerator().make_token(user)
            link  = 'http://localhost:8000/api/v2/reset-password/'+uid+'/'+token
            print('password reset link',link)
            return attrs
        else:
            raise ValidationError('you are not a registered user')

class UserPasswordReset(serializers.Serializer):
    password = serializers.CharField(write_only=True, style={'input_type':'password'})
    password_confirmation = serializers.CharField(write_only=True, style={'input_type':'password'})
    class Meta:
        fields = (
            'password','password_confirmation'
        )
    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password_confirmation= attrs.get('password_confirmation')
            uid=self.context.get('uid')
            token = self.context.get('token')
            if password != password_confirmation:
                raise serializers.ValidationError({"password":"password filed didnt match"})
            id = smart_str(urlsafe_base64_decode(uid))
            try:
                 user = User.objects.get(id=id)
            except Exception:
                raise ValidationError("user does not exsits")
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise ValidationError('token is not valid or expired')
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError:
            raise ValidationError('token is not valid or expired')  

