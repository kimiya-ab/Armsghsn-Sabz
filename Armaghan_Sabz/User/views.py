from django.shortcuts import render
from django.db import models
from rest_framework import serializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from .serializers import    (EditProfileUserSerializer, LoginSerializer, UpdatePassSerializer, 
                            VerificationForgetSerializer, 
                            ForgetPassSerializer, 
                            RegisterSerializer, 
                            UserSerializer,
                            CustomJWTSerializer,
                            PhoneNumberSerializer, 
                            VerificationSerializer,
                            VerifyPhoneNumberOrEmailSerializer,
                            UpdatePhoneNumberSerializer,

                            )
from .models import Profile
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
# from django.contrib.auth.models import User

# for making code and send sms
class PhoneNumberApi(CreateAPIView):
    serializer_class =  PhoneNumberSerializer


# for sending SMS and start registering
class VerificationApi(CreateAPIView):
    serializer_class =  VerificationSerializer
    

class RegisterApi(CreateAPIView):
    serializer_class = RegisterSerializer


# class LoginApi(CreateAPIView):
#     serializer_class = LoginSerializer    

class UserListView(ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'


class ProfileView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'


class EditProfileView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = EditProfileUserSerializer
    lookup_field ='pk'



class EditPhoneNumberApiView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdatePhoneNumberSerializer
    queryset = Profile.objects.all()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


# forget pass with phone/email
class ForgetPassView(CreateAPIView):
    serializer_class = ForgetPassSerializer


# for verify code 
class VerificationForgetApi(CreateAPIView):
    serializer_class =  VerificationForgetSerializer
 

#change pass with phone_number
class UpdatePassPhoneApiView(UpdateAPIView):
    serializer_class = UpdatePassSerializer
    lookup_field = 'phone_number'

    def get_queryset(self):
        query= (str(self.request).split('/'))
        return Profile.objects.filter(phone_number = str(query[3]))
    
