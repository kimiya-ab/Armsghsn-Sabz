import redis
from Armaghan_Sabz.settings import REDIS_PORT, REDIS_HOST, Kavenegar_KEY
from random import randint
from kavenegar import *
from .models import User


rdis = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT, db=0)


# make code for phone_number
def make_verification_code(phone_number):
    code = str(randint(10000,99999))
    pn = phone_number[1:]
    rdis.set(pn, code, 120 )
    print('code is :', code)

    try:
      
        api = KavenegarAPI(Kavenegar_KEY)
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
def verification(phone):

    phone_number = phone[1:]
    if rdis.get(phone_number) == None:
        return 'code expierd'

    verification_code = (rdis.get(phone_number)).decode("utf-8")

    return verification_code


def make_forget_code(phone):
    print(phone)
    code = str(randint(10000,99999))
    print(code)
    # send sms
    if(len(phone) == 11):
        print('phone')
        phone = phone
        user = User.objects.filter(phone_number=phone)

        if len(user) > 0 :
            pn = phone[1:]
            rdis.set(pn, code, 120)

            try:
                api = KavenegarAPI(Kavenegar_KEY)
                params = {
                    'sender': '10004346',#optional
                    'receptor': '+98' + str(pn),#multiple mobile number, split by comma
                    'message': 'برای بازیابی رمز عبور کد زیر را وارد کنید : \n' + str(code),
                } 
                response = api.sms_send(params)
                print(response)

            except APIException as e: 
                print(e)

            except HTTPException as e: 
                print(e)


# this code for make varify code (update email/phone)
def verify_code_update(phone):
    print(phone)
    code = str(randint(10000,99999))
    print(code)


    # send sms
    if (len(phone) == 11):
        phone = phone
        pn = phone[1:]
        rdis.set(pn, code, 120)

        try:
            api = KavenegarAPI(Kavenegar_KEY)
            params = {
                'sender': '10004346',#optional
                'receptor': '+98' + str(pn),#multiple mobile number, split by comma
                'message': 'کداعتبار سنجی : ' + str(code),
            } 
            response = api.sms_send(params)
            print(response)

        except APIException as e: 
                print(e)

        except HTTPException as e: 
                print(e)