from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from user.apps import UserConfig
from django.urls import path
from user.views import UserRegisterAPIView

app_name = UserConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegisterAPIView.as_view(), name='register'),
]
