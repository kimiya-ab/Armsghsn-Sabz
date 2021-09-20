from django.shortcuts import render
from django.db import models
from rest_framework import serializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, permissions
from .serializers import    (EditProfileUserSerializer, UpdatePassSerializer, 
                            VerificationForgetSerializer, 
                            ForgetPassSerializer, 
                            RegisterSerializer, 
                            UserSerializer,
                            CustomJWTSerializer,
                            PhoneNumberSerializer, 
                            VerificationSerializer,
                            CreditCardSerializers,
                            VerifyPhoneNumberOrEmailSerializer,
                            UpdatePhoneNumberSerializer,

                            )
from .models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView


# for making code and send sms
class PhoneNumberApi(CreateAPIView):
    serializer_class =  PhoneNumberSerializer


# for sending SMS and start registering
class VerificationApi(CreateAPIView):
    serializer_class =  VerificationSerializer
    

class RegisterApi(CreateAPIView):
    serializer_class = RegisterSerializer

    

class UserListView(ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'


class ProfileView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'


class EditProfileView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = EditProfileUserSerializer
    lookup_field ='pk'



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


# forget pass with phone/email
class ForgetPassView(CreateAPIView):
    serializer_class = ForgetPassSerializer


# for verify code 
class VerificationForgetApi(CreateAPIView):
    serializer_class =  VerificationForgetSerializer
 

# change pass with email lookup
class UpdatePassApiView(UpdateAPIView):
    serializer_class = UpdatePassSerializer
    lookup_field = 'email'

    def get_queryset(self):
        query= (str(self.request).split('/'))
        return User.objects.filter(email=query[3])


#change pass with phone_number
class UpdatePassPhoneApiView(UpdateAPIView):
    serializer_class = UpdatePassSerializer
    lookup_field = 'phone_number'

    def get_queryset(self):
        query= (str(self.request).split('/'))
        return User.objects.filter(phone_number = str(query[3]))
    

class LoginList(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
 
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)




