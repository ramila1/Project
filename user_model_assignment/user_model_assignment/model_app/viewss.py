
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from .models import CustomUser
# from .serializers import UserSerializer

# class CustomUserListView(APIView):
#     def get(self, request):
#         users = CustomUser.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CustomUserDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             return CustomUser.objects.get(pk=pk)
#         except CustomUser.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, pk):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# from django.http import JsonResponse, HttpResponse
# from django.views import View
# from rest_framework import status
# from .models import CustomUser
# from .serializers import UserSerializer

# class CustomUserListView(View):
#     def get(self, request):
#         users = CustomUser.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     def post(self, request):
#         serializer = UserSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CustomUserDetailView(View):
#     def get_object(self, pk):
#         try:
#             return CustomUser.objects.get(pk=pk)
#         except CustomUser.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, pk):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user)
#         return JsonResponse(serializer.data)

#     def put(self, request, pk):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, data=request.POST, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         user = self.get_object(pk)
#         user.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# from django.http import JsonResponse, HttpResponse
# from django.core.exceptions import ObjectDoesNotExist
# from .models import CustomUser
# from .serializers import UserSerializer
# import json

# def custom_user_list(request):
#     if request.method == 'GET':
#         users = CustomUser.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         user_data = json.loads(request.body)
#         serializer = UserSerializer(data=user_data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# def custom_user_detail(request, pk):
#     try:
#         user = CustomUser.objects.get(pk=pk)
#     except ObjectDoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         user_data = json.loads(request.body)
#         serializer = UserSerializer(user, data=user_data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'PATCH':
#         user_data = json.loads(request.body)
#         serializer = UserSerializer(user, data=user_data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         user.delete()
#         return HttpResponse(status=204)

from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
import json
from base64 import urlsafe_b64encode
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
import jwt,datetime



@csrf_exempt
def custom_user_list(request):
    if request.method == 'POST':
        users = list(CustomUser.objects.values())
        # user_data = [{'id': user.id, 'email': user.email, 'phone': user.phone, 'address': user.address,
        #               'gender': user.gender, 'age': user.age, 'is_staff': user.is_staff, 
        #               'is_active': user.is_active} for user in users]
        
        # print(user_data)
        # return JsonResponse(user_data, safe=False)

    # elif request.method == 'POST':

        # user_data = json.loads(request.body)
        token = request.COOKIES.get("token")
        if token:
            try:
                datam = jwt.decode(token,'ramila',algorithms="HS256")
                return JsonResponse(datam,safe=False,status=400)
            except:
                return JsonResponse("Token not authorized")
        # if users:
        encodejwt = jwt.encode({'msg':'success'},'ramila',algorithm='HS256')
        response = JsonResponse(users,safe=False,status=400)
        response.set_cookie('token',encodejwt)
        return response
        # try:
        #     user = CustomUser.objects.create(email=user_data['email'], phone=user_data['phone'],
        #                                      address=user_data['address'], gender=user_data['gender'],
        #                                      age=user_data['age'], is_staff=user_data.get('is_staff', False),
        #                                      is_active=user_data.get('is_active', True))
        
        #     user.save()
            
        #     return JsonResponse({'id': user.id, 'email': user.email, 'phone': user.phone,
        #                          'address': user.address, 'gender': user.gender, 'age': user.age,
        #                          'is_staff': user.is_staff, 'is_active': user.is_active}, status=201)
        # except KeyError:
        #     return JsonResponse({'error': 'Invalid data provided'}, status=400)

@csrf_exempt
def custom_user_detail(request, pk):
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


# def base64C(data):
#     return urlsafe_b64encode(data).rstrip(b'=')

# def custom_jwt(request):
#     header={
#         "alg": "HS256",
#         "typ": "JWT"
# }
#     payload={
#         "name": "Ramila",
#         "id": 12
# }

# class LoginView():


#         def post(self,request):

        
#             email = request.user_data['email']
#             password = request.user_data['password']

#             user = CustomUser.objects.filter(email=email).first()

#             if user is None:
#                 raise AuthenticationFailed('User not found'
#             )
#             if not user.check_password(password):
#                 raise AuthenticationFailed('Incorrect password')
            
#             payload = {
#                 'id' : user.id,
#                 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#                 'lat':datetime.datetime.utcnow()
#             }

#             token = jwt.encode(payload,'secret',algorithm='HS256').decode('utf-8')
        
#             return Response({
#                 'jwt':token
#         })
    




# from django.views.decorators.csrf import csrf_exempt
# import jwt
# import json
# from django.conf import settings
# from django.http import JsonResponse
# from base64 import urlsafe_b64encode

# def base64C(data):
#     return urlsafe_b64encode(data).rstrip(b'=').decode('utf-8')

# @csrf_exempt
# def custom_jwt(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         user_id = data.get('id')
#         user_name = data.get('name')

#         if not user_id or not user_name:
#             return JsonResponse({'error': 'Invalid data provided'}, status=400)

#         # Define the header and payload
#         header = {
#             "alg": "HS256",
#             "typ": "JWT"
#         }
#         payload = {
#             "name": user_name,
#             "id": user_id
#         }
        
#         # Encode header and payload
#         encoded_header = base64C(json.dumps(header).encode('utf-8'))
#         encoded_payload = base64C(json.dumps(payload).encode('utf-8'))

#         # Create the signature
#         secret = settings.SECRET_KEY
#         signature = jwt.encode(payload, secret, algorithm='HS256').split('.')[2]
        
#         # Create the JWT
#         jwt_token = f"{encoded_header}.{encoded_payload}.{signature}"
        
#         return JsonResponse({'token': jwt_token}, status=200)

        # except Exception:
        #     pass
        # jwt.ExpiredSignatureError:
        #     return JsonResponse({'error': 'Refresh token has expired'}, status=401)
        # except jwt.InvalidTokenError:
        #     return JsonResponse({'error': 'Invalid refresh token'}, status=401)
        # except CustomUser.DoesNotExist:
        #     return JsonResponse({'error': 'User not found'}, status=404)