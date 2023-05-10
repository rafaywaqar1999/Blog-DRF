from django.urls import path
from .views import UserLoginView, UserRegistrationView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('register/', UserRegistrationView.as_view(), name='register-user'),
]
