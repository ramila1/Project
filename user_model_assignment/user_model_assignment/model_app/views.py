from django.http import JsonResponse, HttpResponse, HttpRequest
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from django.contrib.auth.hashers import make_password

from django.shortcuts import get_object_or_404
from django.conf import settings
import json

from django.contrib.auth import authenticate, login as auth_login


class UserList:
    @csrf_exempt
    def custom_user_list(request):
        if request.method == 'GET':
            users = CustomUser.objects.all()
            user_data = [{'id': user.id, 'email': user.email, 'phone': user.phone, 'address': user.address,
                        'gender': user.gender, 'age': user.age, 'is_staff': user.is_staff, 
                        'is_active': user.is_active, 'is_deleted':user.is_deleted, 'deleted_at':user.deleted_at, 'password': user.password} for user in users]
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



class UserDetail:
    @csrf_exempt
    def custom_user_detail(request, pk):
        try:
            user = CustomUser.objects.get(id=pk)
        except CustomUser.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            user_data = {
                'id': user.id,
                'email': user.email,
                'phone': user.phone,
                'address': user.address,
                'gender': user.gender,
                'age': user.age,
                'is_staff': user.is_staff,
                'is_active': user.is_active,
                'is_deleted': user.is_deleted
            }
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
                return JsonResponse({
                    'id': user.id,
                    'email': user.email,
                    'phone': user.phone,
                    'address': user.address,
                    'gender': user.gender,
                    'age': user.age,
                    'is_staff': user.is_staff,
                    'is_active': user.is_active,
                    'is_deleted': user.is_deleted
                })
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
                return JsonResponse({
                    'id': user.id,
                    'email': user.email,
                    'phone': user.phone,
                    'address': user.address,
                    'gender': user.gender,
                    'age': user.age,
                    'is_staff': user.is_staff,
                    'is_active': user.is_active,
                    'is_deleted': user.is_deleted
                })
            except KeyError:
                return JsonResponse({'error': 'Invalid data provided'}, status=400)

        elif request.method == 'DELETE':
            if user.is_deleted:
                try:
                    user.hard_delete()
                    return HttpResponse(status=204)
                except Exception as e:
                    return JsonResponse({'error': str(e)}, status=500)
            else:
                user.soft_delete()
                return HttpResponse(status=204)

class Restore_User:
    @csrf_exempt
    def restore_user(request, pk):
        user = get_object_or_404(CustomUser, pk=pk, is_deleted=True)
        
        if request.method == 'PATCH':
            user.restore()
            return JsonResponse({'message': 'User restored successfully'})
        else:
            return JsonResponse({'error': 'Invalid method'}, status=405)
        


class UserLogin:
    @csrf_exempt
    def login(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            if email and password:
                user = authenticate(request, email=email, password=password)

                if user is not None:
                    auth_login(request, user)
                    return JsonResponse({'message': 'Login successful'})
                else:
                    return JsonResponse({'error': 'Invalid credentials'}, status=400)
            else:
                return JsonResponse({'error': 'Both email and password are required'}, status=400)
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)


