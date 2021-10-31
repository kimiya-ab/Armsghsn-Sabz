from enum import unique
from django.contrib.auth.models import Permission
from django.db import models
from django.db.models import fields, query
from rest_framework import permissions, serializers, status
from rest_framework.fields import empty
from rest_framework.response import Response
from .models import OTP, Profile
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .utils import make_verification_code
from random import randint



# class PhoneNumberSerializer(serializers.Serializer):
#     phone = serializers.CharField(max_length=11)

#     def create(self, validated_data):
#         code = str(randint(10000,99999))
#         if len(validated_data['phone']) == 11 :
#             return validated_data

#         return {'phone': 'your phone number wrong'}

    



class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ('phone_number' , )

    def create(self, validated_data):
            obj = super().create(validated_data )
            obj.code = str(randint(10000,99999))
            obj.save()
            make_verification_code(validated_data['phone_number'] , obj.code)
            return obj 
    


# check sms code with entiry code for login
class VerificationSerializer(serializers.Serializer):
    # phone = serializers.CharField(max_length=11)
    # code = serializers.CharField(max_length=5)
    
    class Meta:
        model = OTP
        fields = '__all__'

    def verify(self , validate_data):
        obj = super().create(validate_data)

    # def create(self, validated_data):
    #     phone = validated_data['phone']
    #     code = validated_data['code']
    #     query = OTP.objects.filter(phone_number = phone , code = code)

        
        # if data == 'code expierd':    
        #     return {'phone':validated_data['phone'], 'code': 'code expierd time'}

        # elif data == validated_data['code']: 
        #     return validated_data
        
        # return {'phone':validated_data['phone'], 'code': 'code is not correct'}



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        extra_kwargs = {
            'password':{'write_only': True},
        }     

    def create(self, validated_data):
        user = Profile.objects.create(
        name = validated_data['name'],
        family = validated_data['family'],
        identity_code = validated_data['identity_code'],
        password = make_password(validated_data['password']), 
        phone_number=validated_data['phone_number'],
        id_number = validated_data['id_number'],
        serial_number = validated_data['serial_number'],
        address = validated_data['address'],
        post_cod = validated_data['post_cod'],
        education = validated_data['education'],
        grade = validated_data['grade'],
        support_phone_number =validated_data['support_phone_number'],
        landline = validated_data['landline'],
        cod_zip = validated_data['cod_zip'],
        profession = validated_data['profession'],
        workplace_address = validated_data['workplace_address'],
        job_position =validated_data['job_position'],
        workplace_number = validated_data['workplace_number'],
        permission = validated_data['permission'] )


        return user

    
class LoginSerializer(serializers.ModelSerializer):
    def validate(self, validated_data):

        if Profile.objects.filter(phone=validated_data['phone_number'],Permission=True):
            pass
        return validated_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        extra_kwargs = {
            'password':{'write_only': True},
        }    



class EditProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'family']
        extra_kwargs = {
            'password':{'write_only': True},
        }     



# you can login with email and phone_number
class CustomJWTSerializer(TokenObtainPairSerializer):
    username_field = 'phone_number'

    def validate(self, attrs):
        credentials = {
            'phone_number': '',
            'password': attrs.get("password")
        }
        user_obj = Profile.objects.filter(phone_number=attrs.get("phone_number")).first()

        if user_obj:
            credentials['phone_number'] = user_obj.phone_number

        return super().validate(credentials)
      


# forget pass send code with phone/email
class ForgetPassSerializer(serializers.Serializer):
    phone = serializers.IntegerField()

    def create(self, validated_data):
        print(validated_data)
        make_forget_code(validated_data['phone'])
        return validated_data



# check sms code with entiry code for login
class VerificationForgetSerializer(serializers.Serializer):
    phone = serializers.IntegerField()
    code = serializers.CharField(max_length=5)
    
    def create(self, validated_data):
        data = verification(validated_data['phone'])

        if data == 'code expierd':    
            return {'phone':validated_data['phone'], 'code': 'code expierd time'}

        elif data == validated_data['code']: 
            return validated_data
        
        return {'phone':validated_data['phone'], 'code': 'code is not correct'}




# update password after get code 
class UpdatePassSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=8)

    class Meta:
        model = Profile
        fields = ['password', 'confirm_password']

    def update(self, instance, validated_data):
        if validated_data['password'] == validated_data['confirm_password']:
            validated_data = {'password': make_password(validated_data['password']), 'confirm_password': validated_data['confirm_password']}

            return super().update(instance, validated_data)

        return {'password': validated_data['password'], 'confirm_password': 'password dose not match !'}
    


# send code with sms/email for varify
class VerifyPhoneNumberOrEmailSerializer(serializers.Serializer):
    phone = serializers.IntegerField()

    def create(self, validated_data):
        print(validated_data)
        verify_code_update(validated_data['phone'])
        return validated_data



class UpdatePhoneNumberSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=5)

    class Meta:
        model = Profile
        fields = ['phone_number', 'code']

    def update(self, instance, validated_data):
        print(validated_data)
        data = verification(validated_data['phone_number'])

        if data == 'code expierd':    
            return {'phone_number':validated_data['phone_number'], 'code': 'code expierd time'}

        elif data == validated_data['code']: 
            # validated_data = {'phone_number': validated_data['phone_number'], 'code': validated_data['code']}
            return super().update(instance, validated_data)
        
        return {'phone_number':validated_data['phone_number'], 'code': 'code is not correct'}