from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework import generics

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

class UserLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
