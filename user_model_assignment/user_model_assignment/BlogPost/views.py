from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from .models import CustomUser, Blog
from django.shortcuts import get_object_or_404
import json

import datetime
import math

import time
from rest_framework.exceptions import AuthenticationFailed


@csrf_exempt
def user_blogs(request: HttpRequest, user_id):
    if request.method == 'GET':
        blogs = Blog.objects.filter(author_id=user_id, is_deleted=False)
        blog_data = [{'id': blog.id, 'title': blog.title, 'description': blog.description, 'published_date': blog.published_date, 'author': blog.author.email} for blog in blogs]
        return JsonResponse(blog_data, safe=False)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def all_blogs(request: HttpRequest):
    if request.method == 'GET':
        blogs = Blog.objects.filter(is_deleted=False)
        blog_data = [{'id': blog.id, 'title': blog.title, 'description': blog.description, 'published_date': blog.published_date, 'author': blog.author.email} for blog in blogs]
        return JsonResponse(blog_data, safe=False)

    elif request.method == 'POST':
        blog_data = json.loads(request.body)
        author_id = blog_data.get('author')
        author = get_object_or_404(CustomUser, id=author_id)
        try:
            blog = Blog.objects.create(title=blog_data['title'], description=blog_data['description'], author=author)
            return JsonResponse({'id': blog.id, 'title': blog.title, 'description': blog.description, 'published_date': blog.published_date, 'author': author.email}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def blog_list(request: HttpRequest):
    if request.method == 'GET':
        blogs = Blog.objects.filter(is_deleted=False)
        blog_data = [
            {
                'id': blog.id,
                'title': blog.title,
                'description': blog.description,
                'published_date': blog.published_date,
                'author': blog.author.email
            } for blog in blogs
        ]
        return JsonResponse(blog_data, safe=False)
    
    elif request.method == 'POST':
        blog_data = json.loads(request.body)
        author_id = blog_data.get('author')
        author = get_object_or_404(CustomUser, id=author_id)
        try:
            blog = Blog.objects.create(
                title=blog_data['title'],
                description=blog_data['description'],
                author=author
            )
            return JsonResponse({
                'id': blog.id,
                'title': blog.title,
                'description': blog.description,
                'published_date': blog.published_date,
                'author': author.email
            }, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

@csrf_exempt
def blog_detail(request: HttpRequest, pk):
    if request.method == 'GET':
        blog = Blog.objects.get(id=pk)
        blog_data = {'id': blog.id, 'title': blog.title, 'description': blog.description, 'published_date': blog.published_date, 'author': blog.author.email}
        return JsonResponse(blog_data)

    elif request.method == 'PUT':
        blog_data = json.loads(request.body)
        try:
            blog = Blog.objects.get(id=pk)
            blog.title = blog_data['title']
            blog.description = blog_data['description']
            blog.save()
            return JsonResponse({'id': blog.id, 'title': blog.title, 'description': blog.description, 'published_date': blog.published_date, 'author': blog.author.email})
        except KeyError:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

    elif request.method == 'PATCH':
        blog_data = json.loads(request.body)
        try:
            blog = Blog.objects.get(id=pk)
            if 'title' in blog_data:
                blog.title = blog_data['title']
            if 'description' in blog_data:
                blog.description = blog_data['description']
            if 'published_date' in blog_data:
                blog.published_date = blog_data['published_date']
            if 'author' in blog_data:
                blog.author = blog_data['author']
            blog.save()
            return JsonResponse({'id': blog.id, 'title': blog.title, 'description': blog.description, 'published_date': blog.published_date, 'author': blog.author.email})
        except KeyError:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

    elif request.method == 'DELETE':
        try:
            blog = Blog.objects.get(id=pk)
            blog.delete()
            return JsonResponse({'message': 'Blog deleted'}, status=204)
        except Blog.DoesNotExist:
            return JsonResponse({'error': 'Blog not found'}, status=404)
    return JsonResponse({'error': 'Method Not Allowed'}, status=405)









