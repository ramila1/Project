from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from .models import CustomUser, Blog
from django.shortcuts import get_object_or_404
import json
import jwt
import datetime
import math
from jwt import ExpiredSignatureError, InvalidTokenError
import time
from rest_framework.exceptions import AuthenticationFailed


# @csrf_exempt
# def all_users(request: HttpRequest):
#     if request.method == 'GET':
#         users = CustomUser.objects.all()
#         user_data = [{'id': user.id, 'email': user.email} for user in users]
#         return JsonResponse(user_data, safe=False)
#     return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def user_blogs(request: HttpRequest, user_id):
    if request.method == 'GET':
        blogs = Blog.objects.filter(author_id=user_id, is_deleted=False)
        blog_data = [{'id': blog.id, 'title': blog.title, 'description': blog.description, 'published_date': blog.published_date, 'author': blog.author.email} for blog in blogs]
        return JsonResponse(blog_data, safe=False)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

# @csrf_exempt
# def all_blogs(request: HttpRequest):
#     if request.method == 'GET':
#         blogs = Blog.objects.filter(is_deleted=False)
#         blog_data = [{'id': blog.id, 'title': blog.title, 'description': blog.description, 'published_date': blog.published_date, 'author': blog.author.email} for blog in blogs]
#         return JsonResponse(blog_data, safe=False)

#     elif request.method == 'POST':
#         blog_data = json.loads(request.body)
#         author_id = blog_data.get('author')
#         author = get_object_or_404(CustomUser, id=author_id)
#         try:
#             blog = Blog.objects.create(title=blog_data['title'], description=blog_data['description'], author=author)
#             return JsonResponse({'id': blog.id, 'title': blog.title, 'description': blog.description, 'published_date': blog.published_date, 'author': author.email}, status=201)
#         except KeyError:
#             return JsonResponse({'error': 'Invalid data provided'}, status=400)
#     return JsonResponse({'error': 'Method not allowed'}, status=405)


# @csrf_exempt
# def blog_list(request: HttpRequest):
#     if request.method == 'GET':
#         blogs = Blog.objects.filter(is_deleted=False)
#         blog_data = [
#             {
#                 'id': blog.id,
#                 'title': blog.title,
#                 'description': blog.description,
#                 'published_date': blog.published_date,
#                 'author': blog.author.email
#             } for blog in blogs
#         ]
#         return JsonResponse(blog_data, safe=False)
    
#     elif request.method == 'POST':
#         blog_data = json.loads(request.body)
#         author_id = blog_data.get('author')
#         author = get_object_or_404(CustomUser, id=author_id)
#         try:
#             blog = Blog.objects.create(
#                 title=blog_data['title'],
#                 description=blog_data['description'],
#                 author=author
#             )
#             return JsonResponse({
#                 'id': blog.id,
#                 'title': blog.title,
#                 'description': blog.description,
#                 'published_date': blog.published_date,
#                 'author': author.email
#             }, status=201)
#         except KeyError:
#             return JsonResponse({'error': 'Invalid data provided'}, status=400)

# @csrf_exempt
# def blog_detail(request: HttpRequest, pk):
#     if request.method == 'GET':
#         blog = Blog.objects.get(id=pk)
#         blog_data = {'id': blog.id, 'title': blog.title, 'description': blog.description, 'published_date': blog.published_date, 'author': blog.author.email}
#         return JsonResponse(blog_data)

#     elif request.method == 'PUT':
#         blog_data = json.loads(request.body)
#         try:
#             blog = Blog.objects.get(id=pk)
#             blog.title = blog_data['title']
#             blog.description = blog_data['description']
#             blog.save()
#             return JsonResponse({'id': blog.id, 'title': blog.title, 'description': blog.description, 'published_date': blog.published_date, 'author': blog.author.email})
#         except KeyError:
#             return JsonResponse({'error': 'Invalid data provided'}, status=400)

#     elif request.method == 'PATCH':
#         blog_data = json.loads(request.body)
#         try:
#             blog = Blog.objects.get(id=pk)
#             if 'title' in blog_data:
#                 blog.title = blog_data['title']
#             if 'description' in blog_data:
#                 blog.description = blog_data['description']
#             if 'published_date' in blog_data:
#                 blog.published_date = blog_data['published_date']
#             if 'author' in blog_data:
#                 blog.author = blog_data['author']
#             blog.save()
#             return JsonResponse({'id': blog.id, 'title': blog.title, 'description': blog.description, 'published_date': blog.published_date, 'author': blog.author.email})
#         except KeyError:
#             return JsonResponse({'error': 'Invalid data provided'}, status=400)

#     elif request.method == 'DELETE':
#         try:
#             blog = Blog.objects.get(id=pk)
#             blog.delete()
#             return JsonResponse({'message': 'Blog deleted'}, status=204)
#         except Blog.DoesNotExist:
#             return JsonResponse({'error': 'Blog not found'}, status=404)
#     return JsonResponse({'error': 'Method Not Allowed'}, status=405)









    

@csrf_exempt
def blog_list(request:HttpRequest):
        token=token_regen_check(request)
        print(token)
        if token:
            if request.method=='GET':
                    if 'all' in request.GET and request.GET['all'].lower() == 'true':
                        blogs=Blog.objects.filter(is_deleted=False)
                    else:
                        refresh_token= request.COOKIES.get("refresh_token")
                        payload=jwt.decode(refresh_token,'secret',algorithms='HS256')
                        author_id = payload.get('id')
                        author = CustomUser.objects.get(id=author_id)
                        blogs = Blog.objects.filter(is_deleted=False, author=author)
                    print(blogs)
                    blog_data = [{
                        'id': blog.id,
                        'title': blog.title, 
                        'description': blog.description,
                        'published_date':blog.published_date,
                        'author': blog.author.email 
                        } for blog in blogs]
                    print(blog_data)
                    return JsonResponse(blog_data, safe=False)
            
            elif request.method == 'POST':
                data = json.loads(request.body)
                refresh_token= request.COOKIES.get("refresh_token")
                payload=jwt.decode(refresh_token,'secret',algorithms='HS256')
                author_id = payload.get('id')
                author = get_object_or_404(CustomUser, id=author_id)
                blog = Blog.objects.create(title=data['title'],description=data['description'],author=author)
                return JsonResponse({'id': blog.id,'title': blog.id, 'description':blog.description,'published_date':blog.published_date, 'author':author.email}, status=201)
            else:
                return JsonResponse({'error': 'Method Not Allowed'}, status=405)
        else:

            return JsonResponse({"check": True})



@csrf_exempt
def blog_detail(request:HttpRequest,pk):
        token=token_regen_check(request)
        if token:
            if request.method=='GET':
                blog = Blog.objects.get(id=pk)
                blog_data ={
                    'id': blog.id,
                    'title': blog.title, 
                    'description': blog.description,
                    'published_date':blog.published_date,
                    'author': blog.author.email
                    } 
                return JsonResponse(blog_data)
            elif request.method == 'PATCH':
                data = json.loads(request.body)
                try:
                    blog = Blog.objects.get(id=pk)
                    blog.title = data['title']
                    blog.description = data['description']
                    blog.save()
                    return JsonResponse({
                        'id': blog.id, 
                        'title': blog.title, 
                        'description': blog.description,
                        'published_date':blog.published_date,
                        'author': blog.author.email
                        })
                except Blog.DoesNotExist:
                    return JsonResponse({'error': ' Blog not found'}, status=404)
            elif request.method == 'DELETE':
                blog = Blog.objects.get(id=pk)
                blog.delete()
                return JsonResponse({'message':'Blog deleted'}, status=204)
            else:
                return JsonResponse({'error': 'Method Not Allowed'}, status=405)
        else:
                return JsonResponse({'error':'Not Authenticated'})
    

@csrf_exempt
def blog_restore(request:HttpRequest,pk):
        token=token_regen_check(request)
        if token:
            if request.method=='POST':
                blog=Blog.objects.get(id=pk)
                blog.restore()
                return JsonResponse({'message':'Blog Restored'}, status=200)
            else:
                return JsonResponse({'error': 'Method Not Allowed'}, status=405)
        else:
                return JsonResponse({'error':'Not Authenticated'})
        

@csrf_exempt
def blog_hard_delete(request:HttpRequest,pk):
        token=token_regen_check(request)
        if token:
            if request.method=='DELETE':
                blog=Blog.objects.get(pk=pk)
                blog.delete(hard_delete=True)
                return JsonResponse({'message':'Blog hard deleted'}, status=204)
        else:
                return JsonResponse({'error':'Not Authenticated'})
        

@csrf_exempt
def token_regen_check(request:HttpRequest):
        token =request.COOKIES.get("access_token")
        print("token generation",token)
        print("token generation",request.COOKIES)   
        if token:
            try:
                payload=jwt.decode(token,"secret",algorithms="HS256")
                user_id=payload.get('id')
                user=CustomUser.objects.get(pk=user_id)
                res={
                        'message':"token Authorization",
                        'data':{
                            'id':user.id,
                            'first_name':user.first_name,
                            'last_name':user.last_name,
                            'email':user.email,
                            'phone_no':user.phone_no,
                            'address':user.address,
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