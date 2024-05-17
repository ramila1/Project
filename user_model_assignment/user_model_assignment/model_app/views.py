from django.http import JsonResponse, HttpResponse, HttpRequest
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import AuthenticationFailed
import jwt
import math
import time
from django.conf import settings
import json
from jwt import ExpiredSignatureError,InvalidTokenError
import datetime


def generate_token(user, token_type, expiry_seconds):
    payload = {
        'type': token_type,
        'id': user.id,
        'email': user.email,
        'exp': math.floor(time.time()) + expiry_seconds,
        'iat': math.floor(time.time())
    }
    return jwt.encode(payload, 'secret', algorithm='HS256')

def decode_token(token):
    return jwt.decode(token,'secret', algorithms=['HS256'])


@csrf_exempt
def custom_user_list(request: HttpRequest):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        user_data = [{'id': user.id, 'email': user.email, 'phone': user.phone, 'address': user.address,
                      'gender': user.gender, 'age': user.age, 'is_staff': user.is_staff, 
                      'is_active': user.is_active, 'password': user.password} for user in users]
        return JsonResponse(user_data, safe=False)

    elif request.method == 'POST':
        user_data = json.loads(request.body)
        password1 = make_password(user_data['password'])
        try:
            user = CustomUser(email=user_data['email'], phone=user_data['phone'],
                              address=user_data['address'], gender=user_data['gender'],
                              age=user_data['age'], is_staff=user_data.get('is_staff', False),
                              is_active=user_data.get('is_active', True), password=password1)
            user.save()
            return JsonResponse({'id': user.id, 'email': user.email, 'phone': user.phone,
                                 'address': user.address, 'gender': user.gender, 'age': user.age,
                                 'is_staff': user.is_staff, 'is_active': user.is_active, 'password': user.password}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

@csrf_exempt
def custom_user_detail(request: HttpRequest, pk):
    try:
        user = CustomUser.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        user_data = {'id': user.id, 'email': user.email, 'phone': user.phone,
                     'address': user.address, 'gender': user.gender, 'age': user.age,
                     'is_staff': user.is_staff, 'is_active': user.is_active}
        return JsonResponse(user_data)

    elif request.method == 'PUT':
        user_data = json.loads(request.body)
        try:
            user.email = user_data['email']
            user.phone = user_data['phone']
            user.address = user_data['address']
            user.gender = user_data['gender']
            user.age = user_data['age']
            user.is_staff = user_data.get('is_staff', False)
            user.is_active = user_data.get('is_active', True)
            user.save()
            return JsonResponse({'id': user.id, 'email': user.email, 'phone': user.phone,
                                 'address': user.address, 'gender': user.gender, 'age': user.age,
                                 'is_staff': user.is_staff, 'is_active': user.is_active})
        except KeyError:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

    elif request.method == 'PATCH':
        user_data = json.loads(request.body)
        try:
            if 'email' in user_data:
                user.email = user_data['email']
            if 'phone' in user_data:
                user.phone = user_data['phone']
            if 'address' in user_data:
                user.address = user_data['address']
            if 'gender' in user_data:
                user.gender = user_data['gender']
            if 'age' in user_data:
                user.age = user_data['age']
            if 'is_staff' in user_data:
                user.is_staff = user_data['is_staff']
            if 'is_active' in user_data:
                user.is_active = user_data['is_active']
            user.save()
            return JsonResponse({'id': user.id, 'email': user.email, 'phone': user.phone,
                                 'address': user.address, 'gender': user.gender, 'age': user.age,
                                 'is_staff': user.is_staff, 'is_active': user.is_active})
        except KeyError:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)



@csrf_exempt
def login(request:HttpRequest):

        if request.method=='POST':
            token =request.COOKIES.get("access_token")
            if token:
                try:
                    payload=jwt.decode(token,"secret",algorithms="HS256")
                    user_id=payload.get('id')
                    user=CustomUser.objects.get(pk=user_id)
                    res={
                        'message':"token Authorization",
                        'data':{
                            'id':user.id,
                            'email':user.email,
                            'phone':user.phone,
                            'address':user.address,
                            'gender':user.gender,
                            'age':user.age
                        }
                    }
                    return JsonResponse(res,status=200)
                 
                except ExpiredSignatureError:
                    response=regenerate(request)
                    return response
                except InvalidTokenError:
                    return JsonResponse({
                        'message':'token invalid',
                    }) 
                
            data = json.loads(request.body)
            email=data['email']
            password=data['password']
            user=CustomUser.objects.filter(email=email).first()
            if user is None:
                raise AuthenticationFailed('User not found')
            if not user.check_password(password):
                raise AuthenticationFailed('Incorrect Password')
            response=token_Generate(request,user)
            return response
        

def token_Generate(request,user):
        access_payload={
                    'type':'access_token',
                    'id':user.id,
                    'email':user.email,
                    'exp': math.floor(time.time())+600,
                    'iat':math.floor(time.time())
                }
        access_token=jwt.encode(access_payload,"secret",algorithm="HS256")
        refresh_payload={
                    'type':'refresh_token',
                    'id':user.id,
                    'email':user.email,
                    'exp': math.floor(time.time())+ 3600,
                    'iat':math.floor(time.time())
                }
        refresh_token=jwt.encode(refresh_payload,"secret",algorithm="HS256")
        response = JsonResponse({'message':'success','access_token':access_token,'refresh_token':refresh_token}, status=200)
        response.set_cookie('access_token',access_token)
        response.set_cookie('refresh_token',refresh_token)
        return response



@csrf_exempt
def regenerate(request:HttpRequest):
        access_token= request.COOKIES.get("access_token")
        refresh_token = request.COOKIES.get('refresh_token')
        now = datetime.datetime.now()
        dt_now =int(now.timestamp())
        if not access_token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            access_payload=jwt.decode(access_token,'secret',algorithms='HS256')
        except jwt.ExpiredSignatureError:
            refresh_payload = jwt.decode(refresh_token,'secret',algorithms='HS256')
            if dt_now < refresh_payload['exp']:
                access_payload={
                    'type':'access',
                    'id':refresh_payload.get('id'),
                    'email':refresh_payload.get('email'),
                    'exp': math.floor(time.time())+600,
                    'iat':math.floor(time.time())
                }
                new_access_token = jwt.encode(access_payload,'secret',algorithm ='HS256')
                refresh_payload={
                    'type':'refresh',
                    'id':refresh_payload.get('id'),
                    'email':refresh_payload.get('email'),
                    'exp': math.floor(time.time())+3600,
                    'iat':math.floor(time.time())
                }
                new_refresh_token = jwt.encode(refresh_payload,'secret',algorithm ='HS256')
                response = JsonResponse({'message':'token regenerate','access token':new_access_token,'refresh token':new_refresh_token},status=204,safe=False)

                
                response.set_cookie('access_token',new_access_token, httponly=True)
                response.set_cookie('refresh_token',new_refresh_token, httponly=True)
              
              

                return response
            else:
                raise AuthenticationFailed('Expired Session')