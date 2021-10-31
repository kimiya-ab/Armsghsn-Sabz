from django.shortcuts import render
from django.db import models
from redis import ResponseError
from rest_framework import serializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView
from .serializers import    (EditProfileUserSerializer, LoginSerializer, OtpSerializer, UpdatePassSerializer, 
                            VerificationForgetSerializer, 
                            ForgetPassSerializer, 
                            RegisterSerializer, 
                            UserSerializer,
                            CustomJWTSerializer,
                            VerificationSerializer,
                            VerifyPhoneNumberOrEmailSerializer,
                            UpdatePhoneNumberSerializer,
                            )
from .models import Profile
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from .utils import make_verification_code
from rest_framework import status , request
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view






# for making code and send sms
class PhoneNumberApi(CreateAPIView):
    serializer_class =  OtpSerializer

        


# for sending SMS and start registering
@api_view(['GET','POST'])
def verificationApi(request):

    data = {
        'phone_number' : request.POST.get('phone_number' , False),
        'code' : request.data['code'],
    }

    ser = VerificationSerializer(data=data)
    if ser.is_valid():
        query = OTP.objects.filter(phone_number=request.POST.get('phone_number' , False))
        if query.exists():
            return Response(status.HTTP_200_OK)
        else:
            return Response(status.HTTP_404_NOT_FOUND)


   
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
    
