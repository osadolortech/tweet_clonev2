
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required=True,write_only=True, validators=[validate_password])
    password_confirmation = serializers.CharField(required=True,write_only=True)
    class Meta:
        model= User
        fields=(
            "first_name","last_name","username","email","password","password_confirmation"
        )
        extra_kwargs= {"first_name":{'required':True}, "last_name":{'required':True}}
    def validate(self, attrs):
        if attrs["password"] != attrs["password_confirmation"]:
            raise serializers.ValidationError({"password": "password fields didnt match"})
        return attrs
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserloginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=123)
    class Meta:
        model=User
        fields=("username","password")

# class ChangeSerializers(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True)
#     new_password = serializers.CharField(write_only=True, required=True,validators=[validate_password])
#     password_confirmation = serializers.CharField(write_only=True, required=True)
#     class Meta:
#         model = User
#         fields = (
#             'password','password_confirmation','new_password'
#         )

#     def validate(self, attrs):
#         user =self.context.get('user')
#         if attrs['password'] == attrs['new_password']:
#             raise serializers.ValidationError({'password': "new_password cant be same as old password"})
#         if attrs['new_password'] != attrs['password_confirmation']:
#             raise serializers.ValidationError({"password":"password filed didnt match"})
#         user.set_password("new_password")
#         user.save()
#         return attrs
