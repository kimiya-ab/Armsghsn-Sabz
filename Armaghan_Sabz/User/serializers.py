from enum import unique
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import  User
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .utils import make_verification_code, verification, make_forget_code, verify_code_update


class PhoneNumberSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11)

    def create(self, validated_data):
        if len(validated_data['phone']) == 11 :
            make_verification_code(validated_data['phone'])
            return validated_data

        return {'phone': 'your phone number wrong'}




# check sms code with entiry code for login
class VerificationSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11)
    code = serializers.CharField(max_length=5)
    
    def create(self, validated_data):
        data = verification(validated_data['phone'])

        if data == 'code expierd':    
            return {'phone':validated_data['phone'], 'code': 'code expierd time'}

        elif data == validated_data['code']: 
            return validated_data
        
        return {'phone':validated_data['phone'], 'code': 'code is not correct'}


class RegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create(
        username = str(validated_data['first_name']) + ' ' + str(validated_data['last_name']) ,
        name = validated_data['first_name'],
        family = validated_data['last_name'],
        identity_code = validated_data['identity_code'],
        # password = make_password(validated_data['password']), 
        phone_number=validated_data['phone_number'],
        id_number = validated_data['id_number'],
        serial_number = validated_data['serial_number'],
        address = validated_data['address'],
        education = validated_data['education'],
        grade = validated_data['grade'],)
        return user

    class Meta:
        model = User
        fields = ('id', 'name', 'family', 'identity_code', 'phone_number', 'id_number', 'serial_number', 'address')
        extra_kwargs = {
            'password':{'write_only': True},
        }     

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password':{'write_only': True},
        }    


class EditProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'fam,ily']
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
        user_obj = User.objects.filter(phone_number=attrs.get("phone_number")).first()

        if user_obj:
            credentials['phone_number'] = user_obj.phone_number

        return super().validate(credentials)
      

# forget pass send code with phone/email
class ForgetPassSerializer(serializers.Serializer):
    phone = serializers.fields.IntegerField(unique= True)

    def create(self, validated_data):
        print(validated_data)
        make_forget_code(validated_data['phone'])
        return validated_data


# check sms code with entiry code for login
class VerificationForgetSerializer(serializers.Serializer):
    phone = serializers.fields.IntegerField(unique= True)
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
        model = User
        fields = ['password', 'confirm_password']

    def update(self, instance, validated_data):
        if validated_data['password'] == validated_data['confirm_password']:
            validated_data = {'password': make_password(validated_data['password']), 'confirm_password': validated_data['confirm_password']}

            return super().update(instance, validated_data)

        return {'password': validated_data['password'], 'confirm_password': 'password dose not match !'}
    


# send code with sms/email for varify
class VerifyPhoneNumberOrEmailSerializer(serializers.Serializer):
    phone = serializers.fields.IntegerField(unique= True)

    def create(self, validated_data):
        print(validated_data)
        verify_code_update(validated_data['phone'])
        return validated_data


class UpdatePhoneNumberSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=5)

    class Meta:
        model = User
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

        
