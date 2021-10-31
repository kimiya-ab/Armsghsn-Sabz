
from Armaghan_Sabz.settings import  Kavenegar_KEY
# from random import randint
from kavenegar import *
from .models import Profile


# rdis = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT, db=0)


# make code for phone_number
def make_verification_code(phone_number , token):
    # code = str(randint(10000,99999))
    code = token
    pn = phone_number
    # rdis.set(pn, code, 120 )
    print('code is :', code)

    try:
      
                # test api with mykey(kimiya)
        # api = KavenegarAPI('514E6D347148396A577234665748586B58484644477748524432497338524B6E41573334485A4E683845303D')
        
        api = KavenegarAPI('514E6D347148396A577234665748586B58484644477748524432497338524B6E41573334485A4E683845303D')
        params = {
            'sender': '10004346',#optional
            'receptor': '+98' + str(pn),#multiple mobile number, split by comma
            'message': 'Wellcome to Armaghan Sabz your verification code is ' + str(code),
        } 
        response = api.sms_send(params)
        print(response)

    except APIException as e: 
        print(e)

    except HTTPException as e: 
        print(e)


# verification method  print('phone')
# def verification(phone):

#     phone_number = phone[1:]
#     if rdis.get(phone_number) == None:
#         return 'code expierd'

#     verification_code = (rdis.get(phone_number)).decode("utf-8")

#     return verification_code


# def make_forget_code(phone):
#     print(phone)
#     code = str(randint(10000,99999))
#     print(code)
#     # send sms
#     if(len(phone) == 11):
#         print('phone')
#         phone = phone
#         user = Profile.objects.filter(phone_number=phone)

#         if len(user) > 0 :
#             pn = phone[1:]
#             rdis.set(pn, code, 120)

#             try:
#                 api = KavenegarAPI('514E6D347148396A577234665748586B58484644477748524432497338524B6E41573334485A4E683845303D')
#                 params = {
#                     'sender': '10004346',#optional
#                     'receptor': '+98' + str(pn),#multiple mobile number, split by comma
#                     'message': 'برای بازیابی رمز عبور کد زیر را وارد کنید : \n' + str(code),
#                 } 
#                 response = api.sms_send(params)
#                 print(response)

#             except APIException as e: 
#                 print(e)

#             except HTTPException as e: 
#                 print(e)


# # this code for make varify code (update email/phone)
# def verify_code_update(phone):
#     print(phone)
#     code = str(randint(10000,99999))
#     print(code)


#     # send sms
#     if (len(phone) == 11):
#         phone = phone
#         pn = phone[1:]
#         rdis.set(pn, code, 120)

#         try:
#             api = KavenegarAPI('514E6D347148396A577234665748586B58484644477748524432497338524B6E41573334485A4E683845303D')
#             params = {
#                 'sender': '10004346',#optional
#                 'receptor': '+98' + str(pn),#multiple mobile number, split by comma
#                 'message': 'کداعتبار سنجی : ' + str(code),
#             } 
#             response = api.sms_send(params)
#             print(response)

#         except APIException as e: 
#                 print(e)

#         except HTTPException as e: 
#                 print(e)