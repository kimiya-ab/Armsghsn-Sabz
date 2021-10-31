from django.urls import path
from django.views.generic.base import View
from rest_framework import views
from .views import *
from .serializers import CustomJWTSerializer
from rest_framework_simplejwt.views import (TokenObtainPairView , TokenRefreshView)
from . import views



urlpatterns = [
    path('phone/', PhoneNumberApi.as_view(), name='register-phone'),
    # path('phone/<str:phone_number>/', VerificationApi.as_view(), name='varification-code'),
    path('otp/', views.verificationApi),
    path('phone/<str:phone_number>/register/', RegisterApi.as_view(), name='register-user'),
    path('register/', RegisterApi.as_view(), name='register'),
    path('user/', UserListView.as_view(), name='all-user'),
    path('user/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('user/<int:pk>/edit/', EditProfileView.as_view(), name='edit-profile'),
    path('user/<int:pk>/edit/phone/update/', EditPhoneNumberApiView.as_view(), name='edit-phone'),
    path('token/', MyTokenObtainPairView.as_view(serializer_class=CustomJWTSerializer)),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('forget/', ForgetPassView.as_view(), name= 'forget-pass'),
    path('forget/code/',VerificationForgetApi.as_view(), name= 'forget-pass-code'),
    path('forget/<int:phone_number>/phone/update/', UpdatePassPhoneApiView.as_view(), name= 'update-pass-phone'),
]
