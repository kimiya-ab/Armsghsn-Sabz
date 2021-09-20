from django.urls import path
from .views import *
from .serializers import CustomJWTSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('phone/', PhoneNumberApi.as_view(), name='register-phone'),
    path('phone/<str:phone_number>/', VerificationApi.as_view(), name='varification-code'),
    path('phone/<str:phone_number>/register/', RegisterApi.as_view(), name='register-user'),
    path('register/', RegisterApi.as_view(), name='register'),
]