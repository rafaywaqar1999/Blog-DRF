from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username')
class LoginSerializer(TokenObtainPairSerializer):
    username_field = 'username'

    def validate(self, data):
        credentials = {
            'username': data.get('username'),
            'password': data.get('password')
        }
        if all(credentials.values()):
            user = authenticate(**credentials)
            if user:
                refresh = self.get_token(user)
                data = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user' : UserSerializer(user).data
                }
                return data
            else:
                raise serializers.ValidationError('Incorrect/Invalid username or password')
        else:
            raise serializers.ValidationError('Must provide username and password')


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if len(username) < 8 or len(password) < 8:
            raise serializers.ValidationError('Username and password must be of lenght 8')
        return data
    
    def create(self, validated_data):
        user = CustomUser(
            username=validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


