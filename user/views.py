from rest_framework import generics
from rest_framework.permissions import AllowAny
from user.serializers import UserSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    """'Эндпоинт создания пользователя"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
